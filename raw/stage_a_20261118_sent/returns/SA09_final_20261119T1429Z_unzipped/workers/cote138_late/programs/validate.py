"""Structural audit only; it does not manufacture or validate semantic verdicts."""
import csv,hashlib,json,re,sys
from collections import Counter
from pathlib import Path
import sympy
B=Path(__file__).resolve().parents[1]
ROOT=B.parents[2]
SRC=ROOT/'source'/'SA09_texts'/'pro'
def table(name):return list(csv.DictReader((B/name).open(),delimiter='\t'))
entries=table('entries.tsv');items=json.loads((B/'items.json').read_text());claims=json.loads((B/'claims.json').read_text());problems=json.loads((B/'problems.json').read_text());readings=table('readings.tsv');search=table('search_log.tsv');events=table('CHECK_EVENTS.tsv')
expected=[f'MPL_138_090-133#{n}' for n in range(1,128)]
assert len(entries)==127 and Counter(x['entry_id'] for x in entries)==Counter(expected)
assert Counter(s for i in items for s in i['sources'])==Counter(expected)
index=list(csv.DictReader((ROOT/'SA09_work'/'global_index.tsv').open(),delimiter='\t'))
ordinal={x['entry_id']:int(x['ordinal']) for x in index}
for item in items:assert item['id']==f"SA09-{min(ordinal[s] for s in item['sources'])}"
I={i['id']:i for i in items};C={c['id']:c for c in claims};P={p['id']:p for p in problems}
assert len(I)==len(items)==66 and len(C)==len(claims)==82 and len(P)==len(problems)==24
assert set(C)=={f'CL-SA09-138L-{n:03}' for n in range(1,83)}
assert set(P)=={f'MP-SA09-{n}' for n in range(70,94)}
fields={
'items.json':'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),
'claims.json':'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),
'problems.json':'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()}
for name,keys in fields.items():
 for x in json.loads((B/name).read_text()):assert set(x)==set(keys),(name,x['id'],set(x)^set(keys))
for e in entries:assert e['item_id'] in I and e['entry_id'] in I[e['item_id']]['sources']
for c in claims:
 assert set(c['items'])<=set(I),(c['id'],c['items'])
 assert c['class'] in 'ABCDEF' and c['confidence'] in ['high','medium','low']
 assert all(c[k] for k in fields['claims.json'])
for p in problems:
 assert p['occurrences'] and p['state_of_art'] and p['refs']
 for o in p['occurrences']:
  assert o['claim'] in C and set(o['items'])<=set(I)
refs=set(re.findall(r'@\w+\{([^,]+),',(B/'references.bib').read_text()))
assert len(refs)==24
used={r for c in claims for r in c['refs']}|{r for p in problems for r in p['refs']}
assert used<=refs,used-refs
assert Counter(x['claim_id'] for x in search)==Counter(C.keys())
for r in search:assert r['queries'] and r['exact_scope'] and r['opened_results'] and r['outcome']
covered={x['statement_id'] for x in events}
assert set(I)|set(C)|refs<=covered,(set(I)|set(C)|refs)-covered
eventtypes={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted, with refined statement id'}
assert {x['type'] for x in events}<=eventtypes

source_cache={}
def source(name):
 if name not in source_cache:
  path=SRC/Path(name).name
  lines=path.read_text().splitlines();current=None;scans={}
  for number,line in enumerate(lines,1):
   m=re.search(r'\\scanpage\{(\d+)\}',line)
   if m:current=int(m.group(1))
   scans[number]=current
  source_cache[name]=(lines,scans)
 return source_cache[name]
warnings=[]
def locus(loc,declared,owner):
 name,nums=loc.rsplit(':',1);lines,scans=source(name)
 actual=set()
 for part in nums.replace('–','-').split(','):
  a,*rest=part.split('-');a=int(a);z=int(rest[0]) if rest else a
  assert 1<=a<=z<=len(lines),(owner,loc,len(lines))
  actual.update(scans[n] for n in range(a,z+1))
 actual.discard(None)
 missing=actual-set(map(int,declared))
 if missing:warnings.append({'owner':owner,'locus':loc,'source_scans_missing_from_record':sorted(missing),'declared':declared})
for o in items+claims:
 for loc in o['lines']:locus(loc,o['scans'],o['id'])
for p in problems:
 for o in p['occurrences']:
  for loc in o['lines']:locus(loc,o['scans'],p['id'])
for n,r in enumerate(readings,1):locus(r['line'],[r['scan']],f'reading-{n}')
for filename in ['links.tsv','project_leads.tsv','verified_project_links.tsv']:
 for row in table(filename):
  assert set(row)=={'kind','from','to','what','evidence','note_ids'} and row['kind'] in ['folder','published work','our projects']
  assert row['from'] and row['to'] and row['evidence'] and row['note_ids']
  assert set(row['note_ids'].split('; '))<=set(expected)
assert len(table('links.tsv'))==15 and len(table('project_leads.tsv'))==41
assert not table('verified_project_links.tsv')
for filename in ['synthesis.md','directions.md','proofs.md','search_coverage.md','review_response.md']:
 assert (B/filename).stat().st_size>500
for filename in ['exact_arithmetic.json','finite_maps_all.json','finite_maps_summary.json','catalogue_checks.json']:
 json.loads((B/'outputs'/filename).read_text())
assert json.loads((B/'outputs'/'catalogue_checks.json').read_text())['claims_checked']==29
assert json.loads((B/'outputs'/'finite_maps_summary.json').read_text())['number_total']==77
directions=(B/'directions.md').read_text()
assert len(re.findall(r'^## \d+\.',directions,re.M))==12
counts={'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),'readings':len(readings),'directions':12,'verified_links':15,'reported_project_leads':41,'verified_project_file_links':0,'references':len(refs),'search_rows':len(search),'check_events':len(events),'item_kinds':dict(Counter(i['kind'] for i in items)),'item_checks':dict(Counter(i['check'] for i in items)),'claim_classes':dict(Counter(c['class'] for c in claims)),'claim_statuses_verbatim':dict(Counter(c['status_on_pages'] for c in claims)),'entry_verdicts':dict(Counter('merged' if x['verdict'].startswith('merged') else x['verdict'] for x in entries)),'source_locator_warnings':warnings,'runtime':{'python':sys.version,'sympy':sympy.__version__}}
(B/'outputs'/'coverage_counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False,indent=2))
assert not warnings,'Resolve source-scan locator mismatches listed above.'
print('PASS: schema, exact entry partition, identifiers, citations, per-claim searches, check-event coverage and source bounds. This is not an automated semantic verdict.')
