"""Final deliverable coverage gate, not a machine proof of the mathematics."""
from pathlib import Path
import json,csv,re,collections,hashlib
R=Path(__file__).resolve().parents[1]
def jr(name):return json.loads((R/name).read_text())
def tr(name):
    with (R/name).open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
errors=[];checks=[]
def check(name,condition,detail=None):
    checks.append({'check':name,'passed':bool(condition),'detail':detail})
    if not condition:errors.append(name)
required=['SA21_dossier.md','SA21_entries.tsv','SA21_items.json','SA21_claims.json','SA21_problems.json','SA21_readings.tsv','SA21_links.tsv','SA21_project_leads.tsv','SA21_unresolved_links.tsv','SA21_directions.md','SA21_references.bib','CHECK_EVENTS.tsv','progress.log','SA21_search_map.tsv','SA21_coverage.tsv','README.md']
check('All principal deliverables exist',all((R/p).is_file() and (R/p).stat().st_size for p in required))
entries=tr('SA21_entries.tsv');items=jr('SA21_items.json');claims=jr('SA21_claims.json');problems=jr('SA21_problems.json')
expected={f'MPL_156-1+156-2#{n}' for n in range(1,123)}
check('All122 source entries exactly once',len(entries)==122 and {e['entry_id'] for e in entries}==expected)
all_sources=[s for x in items for s in x['sources']]
check('All122 source entries in exactly one consolidated item',len(all_sources)==122 and set(all_sources)==expected)
ids={x['id'] for x in items};cids={x['id'] for x in claims};pids={x['id'] for x in problems}
check('Unique item, claim and problem IDs',len(ids)==len(items) and len(cids)==len(claims) and len(pids)==len(problems))
byitem={x['id']:x for x in items}
check('Entry pointers match actual item membership',all(e['item_id'] in ids and e['entry_id'] in byitem[e['item_id']]['sources'] for e in entries))
schema={
 'items':['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],
 'claims':['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],
 'problems':['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']}
for name,data in [('items',items),('claims',claims),('problems',problems)]:
    missing={x.get('id','?'):[f for f in schema[name] if f not in x] for x in data}
    missing={k:v for k,v in missing.items() if v}
    check(name+' required fields',not missing,missing)
check('Claim item pointers exist',all(set(c['items'])<=ids for c in claims))
check('All six fate classes valid',all(c['class'] in 'ABCDEF' and len(c['class'])==1 for c in claims))
statuses={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages','definition/construction','current-run refinement'}
check('No pending primary status category',all(c.get('status_category') in statuses for c in claims))
check('Claim fate and present-status fields populated',all(c['fate'] and c['present_status'] and c['fate_date'] for c in claims))
search=tr('SA21_search_map.tsv')
check('Every claim mapped to executed searches exactly once',len(search)==len(claims) and {s['claim_id'] for s in search}==cids and all(s['search_ids'] and s['queries_and_locators'] for s in search))
check('No missing searches in assembly audit',not jr('audit/search_coverage.json')['missing_claim_ids'])
bib=(R/'SA21_references.bib').read_text();blocks=[b for b in re.split(r'(?=^@)',bib,flags=re.M) if re.match(r'@\w+\{',b)]
bkeys=[];notes={}
for b in blocks:
    key=re.match(r'@\w+\{\s*([^,]+)',b)[1].strip();bkeys.append(key)
    m=re.search(r'\bnote\s*=\s*\{([^{}]*)\}',b);notes[key]=m[1].strip() if m else None
check('Bibliography keys unique',len(bkeys)==len(set(bkeys)))
check('Every bibliography has literal verified/unverified note',all(v in ['verified','unverified'] for v in notes.values()),{k:v for k,v in notes.items() if v not in ['verified','unverified']})
unknown_refs=sorted({k for x in claims+problems for k in x['refs'] if k not in bkeys})
check('All claim/problem bibliography keys resolve',not unknown_refs,unknown_refs)
events=tr('CHECK_EVENTS.tsv');event_ids={e['statement_id'] for e in events}
check('Every claim has a check-event record',cids<=event_ids,sorted(cids-event_ids))
check('Every consolidated item has a source-check event',ids<=event_ids,sorted(ids-event_ids))
check('Every bibliographic key has an explicitly scoped event',set(bkeys)<=event_ids,sorted(set(bkeys)-event_ids))
allowed_events={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted, with the refined statement’s id'}
check('Event types describe the requested actual check types',all(e['type'] in allowed_events for e in events),sorted({e['type'] for e in events}-allowed_events))
unpointed=[]
for e in events:
    if e['type'].startswith('refuted') and not re.search(r'(?:C-SA21-|R-SA21-|MP-SA21-)',e['outcome']):unpointed.append(e['statement_id'])
check('Every refutation points to a named refinement or scoped problem',not unpointed,unpointed)
coverage=jr('audit/coverage_summary.json')
check('Full supplied file inventory:82Codex+1Pro',coverage['Codex_folders']==82 and coverage['Pro_packages']==1 and coverage['folders']==83 and len(tr('SA21_coverage.tsv'))==83)
check('All nine cotes represented',set(c['cote'] for c in claims)=={f'156-{i}' for i in range(1,10)})
check('Missing supplied scan ranges explicitly recorded',[(c['cote'],c['missing_catalogue_scan_numbers']) for c in coverage['by_cote'] if c['missing_catalogue_scan_numbers']]==[('156-7',list(range(2,10))),('156-9',[129])])
directions=jr('audit/directions.json')
check('Every ranked direction has existing item/claim/problem origins',all(d['items'] and d['claims'] and d['problems'] and set(d['items'])<=ids and set(d['claims'])<=cids and set(d['problems'])<=pids for d in directions))
check('Direction ranks consecutive',sorted(d['rank'] for d in directions)==list(range(1,len(directions)+1)))
links=tr('SA21_links.tsv')
check('Only checked folder/publication kinds in main link table',all(x['kind'] in ['folder','published work'] for x in links))
check('Main link note_ids contain source-note IDs only',all(not re.search(r'(?:C-SA21-|MP-SA21-)',x.get('note_ids','')) for x in links))
project=tr('SA21_project_leads.tsv')
check('All54 other-project target records retained separately',len(project)==54)
check('All125 Context paragraphs audited',len(tr('parts/project_links/context_coverage.tsv'))==125)
for part,n in [('root',80),('cotes_3_5',99),('cotes_6_7',96),('cotes_8_9',87),('cotes_9_09_13',36)]:
    check('Expected stable claim block '+part,len(jr('parts/'+part+'/claims.json'))==n)
check('IX final block complete through128',set(f'C-SA21-9-{i:03d}' for i in range(81,129))<={c['id'] for c in jr('parts/cotes_9_14_18/claims.json')})
for part in ['cotes_3_5','cotes_6_7','cotes_8_9','cotes_9_09_13','cotes_9_14_18']:
    names=['claims.json','problems.json','readings.tsv','links.tsv','check_events.tsv','search_log.tsv','coverage.tsv','references.bib','narrative.md']
    check('Complete owned deliverables '+part,all((R/'parts'/part/n).exists() for n in names))
check('No awaiting-owner wording in principal dossier',not re.search(r'awaiting explicit owner|awaiting inspection of the continuation', (R/'SA21_dossier.md').read_text(),flags=re.I))
report={'validation':'PASS' if not errors else 'FAIL','checks':checks,'failures':errors,
 'counts':{'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),'readings':len(tr('SA21_readings.tsv')),'directions':len(directions),'references':len(bkeys),'check_events':len(events)},
 'bibliography_status':dict(collections.Counter(notes.values())),
 'scope':'This validates coverage, identifiers, evidence pointers and packaging prerequisites. It does not turn reading into proof or establish an exhaustive negative literature theorem.'}
(R/'audit/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'validation':report['validation'],'checks':len(checks),'failures':errors,'counts':report['counts']},ensure_ascii=False,indent=2))
assert not errors,'Resolve concrete deliverable gaps before final packaging.'
