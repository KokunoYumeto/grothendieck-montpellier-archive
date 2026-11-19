"""Structural validation only; this does not manufacture mathematical verdicts."""
import csv,json,pathlib,collections,datetime
B=pathlib.Path(__file__).resolve().parents[1]
def j(n):return json.loads((B/n).read_text())
def t(n):return list(csv.DictReader((B/n).open(),delimiter='\t'))
I=j('items.json');C=j('claims.json');P=j('problems.json');R=j('references.json');E=t('entries.tsv');A=t('CHECK_EVENTS.tsv');S=t('search_log.tsv')
expected={f'MPL_57_089-132#{n}'for n in range(1,73)}|{f'MPL_57_226-270#{n}'for n in range(1,84)}
ii={x['id']for x in I};cc={x['id']for x in C};pp={x['id']for x in P};rr={x['key']for x in R};ss={x['search_id']for x in S};ee={x['statement_id']for x in A}
assert len(E)==155 and{e['entry_id']for e in E}==expected
assert len(I)==len(ii)==95 and len(C)==len(cc)==142 and len(P)==len(pp)==54 and len(R)==len(rr)==39
assert set(s for i in I for s in i['sources'])==expected
assert sum(len(i['sources'])for i in I)==155
for e in E:
 assert e['item_id']in ii and e['reason']and e['verdict']in{'kept','merged','corrected','withdrawn','rests on a misreading'}
 assert e['entry_id']in next(i for i in I if i['id']==e['item_id'])['sources']
for c in C:
 assert set(c['items'])<=ii and set(c['refs'])<=rr and set(c['search_events'])<=ss and c['search_events']
 assert c['class']in'ABCDEF'and all(c[k]for k in['lines','his_statement','statement','status_on_pages','fate','present_status','confidence','witness_type'])
 for sid in c['search_events']:assert c['id']in next(x for x in S if x['search_id']==sid)['claim_ids'].split(';')
for p in P:
 assert set(p['claims'])<=cc and set(p['items'])<=ii and set(p['refs'])<=rr
 assert all(p[k]for k in['title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth'])
assert ii|cc|rr<=ee
assert all(r['note']=='verified'and r['url']and r['checked_locator']and r['verification_scope']for r in R)
assert not list(B.rglob('*.pdf')),'Whole external PDFs must stay outside deliverables.'
required=['entries.tsv','items.json','claims.json','problems.json','readings.tsv','links.tsv','project_leads.tsv','directions.md','references.bib','CHECK_EVENTS.tsv','search_log.tsv','read_log.tsv','synthesis.md','computations.md']
assert all((B/n).is_file()and(B/n).stat().st_size>0 for n in required)
calc=j('outputs/calculation_run.json');assert calc['all_exact_assertions_passed']and calc['calculation_groups']==len(j('outputs/calculations.json'))
result=dict(checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),structural_checks='passed',scope='Checks only coverage, identifiers, joins, required fields and saved calculation receipts; not a proof certificate for claims.',entries=len(E),items=len(I),claims=len(C),problems=len(P),readings=len(t('readings.tsv')),checked_links=len(t('links.tsv')),quarantined_project_leads=len(t('project_leads.tsv')),references=len(R),search_groups=len(S),check_events=len(A),read_chunks=len(t('read_log.tsv')),calculation_groups=calc['calculation_groups'],verdict_counts=dict(collections.Counter(e['verdict']for e in E)),claim_classes=dict(collections.Counter(c['class']for c in C)))
(B/'outputs/validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
