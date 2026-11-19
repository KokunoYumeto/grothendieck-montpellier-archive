"""Check record integrity and coverage, never mathematical verdicts."""
import csv,hashlib,json,re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WS=ROOT.parents[2]
items=json.loads((ROOT/'items.json').read_text())
claims=json.loads((ROOT/'claims.json').read_text())
problems=json.loads((ROOT/'problems.json').read_text())
def read_tsv(name):
 return list(csv.DictReader((ROOT/name).open(),delimiter='\t'))
entries=read_tsv('entries.tsv')
coverage=read_tsv('claim_search_coverage.tsv')
events=read_tsv('check_events.tsv')
readings=read_tsv('readings.tsv')
links=read_tsv('links.tsv')
required={
 'items':['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],
 'claims':['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],
 'problems':['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']}
for name,data in [('items',items),('claims',claims),('problems',problems)]:
 assert len({r['id'] for r in data})==len(data),name+' duplicate IDs'
 for r in data: assert set(required[name])<=set(r),(name,r['id'])
all_index=list(csv.DictReader((WS/'sources'/'SA16_notes'/'NOTES_INDEX.tsv').open(),delimiter='\t'))
wanted={r['entry_id'] for r in all_index if r['package'] in ('MPL_64_002-039','MPL_64_040-077')}
assert len(wanted)==129
assert len(entries)==129 and {r['entry_id'] for r in entries}==wanted
assert len({r['entry_id'] for r in entries})==129
source_ids=[e for r in items for e in r['sources']]
assert len(source_ids)==129 and len(set(source_ids))==129 and set(source_ids)==wanted
item_ids={r['id'] for r in items}; claim_ids={r['id'] for r in claims}
assert all(r['item_id'] in item_ids for r in entries)
assert all(set(r['items'])<=item_ids for r in claims)
assert {r['claim_id'] for r in coverage}==claim_ids and len(coverage)==len(claims)
assert all(r['exact_search_ids'] for r in coverage)
assert all(r['opened_followup_ids'] for r in coverage)
event_ids={r['statement_id'] for r in events}
assert item_ids|claim_ids<=event_ids
keys=set(re.findall(r'@\w+\{([^,]+),',(ROOT/'references.bib').read_text()))
assert set(k for r in claims+problems for k in r['refs'])<=keys
assert keys<=event_ids

locator_warnings=[]
for r in items+claims:
 for loc in r['lines']:
  p=WS/'sources'/'SA16_texts'/'pro'/loc['file']
  lines=p.read_text().splitlines()
  assert 1<=loc['start']<=loc['end']<=len(lines),(r['id'],loc)
  if 'scan' in loc:
   active=None
   for line in lines[:loc['start']]:
    m=re.search(r'\\scanpage\{(\d+)\}',line)
    if m: active=int(m.group(1))
   scans={active}|{int(x) for line in lines[loc['start']-1:loc['end']] for x in re.findall(r'\\scanpage\{(\d+)\}',line)}
   if loc['scan'] not in scans: locator_warnings.append({'id':r['id'],'location':loc,'active_scans':sorted(x for x in scans if x is not None)})
assert not locator_warnings,locator_warnings

# Confirm the raw web text and full external PDFs are outside this deliverable.
for p in (ROOT/'outputs').glob('web_*.json'):
 a=json.loads(p.read_text());assert 'result' not in a and 'researcher_outcome' in a
assert not list(ROOT.rglob('*.pdf'))
for file in ['finite_groups','cube_and_pgl','symbolic_checks','kummer_counterexample','scalar_quotient']:
 assert (ROOT/'code'/f'{file}.py').exists() and (ROOT/'outputs'/f'{file}.json').exists()
verdicts=Counter(r['verdict'].split(' (')[0].split(' into')[0] for r in entries)
result={
 'run':'SA16-2026-11-19-cote64-early','date':'2026-11-19','schema_and_coverage_checks':'passed',
 'entries':len(entries),'by_package':dict(Counter(r['entry_id'].split('#')[0] for r in entries)),
 'items':len(items),'item_kinds':dict(Counter(r['kind'] for r in items)),
 'verdict_counts':dict(verdicts),'text_comparison_counts':dict(Counter(r['check'] for r in items)),
 'claims':len(claims),'claims_by_class':dict(Counter(r['class'] for r in claims)),
 'claims_by_exact_page_status':dict(Counter(r['status_on_pages'] for r in claims)),
 'problems':len(problems),'readings':len(readings),
 'verified_links':sum(r['verification']=='both endpoints checked' for r in links),
 'prior_context_leads':sum(r['verification'].startswith('prior context') for r in links),
 'references':len(keys),'search_log_rows':len(read_tsv('search_log.tsv')),
 'claim_search_coverage_rows':len(coverage),'check_events':len(events),
 'directions':7,'locator_warnings':locator_warnings,
 'limits':['No scans; ink alternatives unresolved.','Unavailable project endpoints remain leads.','Ledet exact section and original Lattes1918 not used as verified results.','General repaired varying-group Kummer equivalence not asserted.'],
 'validation_scope':'Structural integrity and declared coverage only; no mathematical verdict is inferred by this program.'}
(ROOT/'coverage.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(ROOT/'outputs'/'validate_package.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['schema_and_coverage_checks','entries','items','claims','problems','readings','verified_links','prior_context_leads','references','search_log_rows','check_events']},indent=2))
