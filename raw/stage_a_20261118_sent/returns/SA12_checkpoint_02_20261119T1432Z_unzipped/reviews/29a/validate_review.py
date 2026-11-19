"""Structural audit only; semantic judgments were made by manual reading."""
import json,csv,re,collections
from pathlib import Path
P=Path(__file__).parent
def js(name): return json.loads((P/(name+'.json')).read_text())
def ts(name): return list(csv.DictReader((P/(name+'.tsv')).open(),delimiter='\t'))
I,C,O=js('items'),js('claims'),js('problems')
E,R,L,V=ts('entries'),ts('readings'),ts('links'),ts('CHECK_EVENTS')
required={
'items':{'id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'},
'claims':{'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'},
'problems':{'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}}
for name,rows in [('items',I),('claims',C),('problems',O)]:
 assert all(set(r)==required[name] for r in rows),name
 assert len({r['id'] for r in rows})==len(rows),name
ii={x['id'] for x in I};cc={x['id'] for x in C};oo={x['id'] for x in O}
assert len(E)==129
assert {e['entry_id'] for e in E}=={f'MPL_29_049-094#{n}' for n in range(1,130)}
assert all(e['item_id'] in ii for e in E)
source_map={s:i['id'] for i in I for s in i['sources']}
assert len(source_map)==129
assert all(source_map[e['entry_id']]==e['item_id'] for e in E)
assert all(set(c['items'])<=ii for c in C)
assert all(o['item'] in ii for p in O for o in p['occurrences'])
keys=set(re.findall(r'^@\w+\{([^,]+),',(P/'references.bib').read_text(),re.M))
assert all(set(c['refs'])<=keys for c in C)
assert all(set(p['refs'])<=keys for p in O)
sm=js('claim_search_map')
assert {x['claim_id'] for x in sm}==cc
assert all(x['batches'] for x in sm)
assert all((P/f).exists() for x in sm for f in x['batches'])
assert all(l['kind'] in ['folder','published work','our projects'] for l in L)
assert all(v['statement_id'] in ii|cc|keys for v in V)
allowed=['targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found']
assert all(v['type'] in allowed or v['type'].startswith("refuted, with refined statement's id ") for v in V)
for row in (P/'directions.md').read_text().splitlines():
 if re.match(r'\| \d+ \|',row):
  assert 'SA12-' in row and 'CL-SA12-' in row and 'MP-SA12-' in row,row
counts={
'entries':len(E),'items':len(I),'verdicts':dict(collections.Counter(x['verdict'] for x in E)),
'item_kinds':dict(collections.Counter(x['kind'] for x in I)),
'text_checks':dict(collections.Counter(x['check'] for x in I)),
'claims':len(C),'claim_classes':dict(collections.Counter(x['class'] for x in C)),
'claim_statuses_exact':dict(collections.Counter(x['status_on_pages'] for x in C)),
'problems':len(O),'readings':len(R),'links':len(L),'links_by_kind':dict(collections.Counter(x['kind'] for x in L)),
'directions':10,'references':len(keys),'check_events':len(V),
'search_batches':len(list(P.glob('web_batch_*.json'))),
'search_calls':len(ts('SEARCH_CALLS')),'returned_search_records':len(ts('SEARCH_RESULTS')),
'scope':'Package-local counts before parent cross-package consolidation; no global-uniqueness assertion.'}
(P/'COUNTS.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False,indent=2))
print('Structural audit passed. This is not a semantic proof certificate.')
