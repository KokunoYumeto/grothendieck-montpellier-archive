"""Reproducible structural audit, not a script for generating mathematical verdicts."""
import collections,csv,json,pathlib,re
R=pathlib.Path('SA05/work/cote11a')
def j(n):return json.loads((R/n).read_text())
def t(n):return list(csv.DictReader((R/n).open(),delimiter='\t'))
items=j('items.json');claims=j('claims.json');problems=j('problems.json');entries=t('entries.tsv');readings=t('readings.tsv');links=t('links.tsv');search=t('search_log.tsv');events=t('CHECK_EVENTS.tsv');refs=j('references_metadata.json')
expected={r['entry_id'] for r in csv.DictReader(open('sources/notes/NOTES_INDEX.tsv'),delimiter='\t') if r['package']=='MPL_11_002-042'}
assert len(entries)==82 and {e['entry_id'] for e in entries}==expected
assert len({e['entry_id'] for e in entries})==82
required={
 'items':['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],
 'claims':['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],
 'problems':['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']}
for name,objects in [('items',items),('claims',claims),('problems',problems)]:
 assert len({x['id'] for x in objects})==len(objects)
 for x in objects:assert all(k in x for k in required[name]),(name,x['id'])
ii={x['id'] for x in items};ci={x['id'] for x in claims};pi={x['id'] for x in problems};ri={x['key'] for x in refs};si={x['search_id'] for x in search}
for e in entries:assert e['item_id'] in ii
covered=set()
for x in items:
 assert set(x['sources'])<=expected
 covered|=set(x['sources'])
assert covered==expected
for c in claims:
 assert set(c['items'])<=ii and set(c['refs'])<=ri
 assert c['class'] in 'ABCDEF' and c['search_ids'] and set(c['search_ids'])<=si
 for sid in c['search_ids']:
  row=next(s for s in search if s['search_id']==sid)
  assert c['id'] in row['claim_ids'].split(';')
for p in problems:
 assert set(p['refs'])<=ri and set(p.get('claim_ids',[]))<=ci
assert ci|ii|ri <= {x['statement_id'] for x in events}
assert {r['kind'] for r in links}<={'folder','published work','our projects'}
for row in readings:
 fn,ls=row['line'].rsplit(':',1);lines=pathlib.Path(fn).read_text().splitlines();a,*b=map(int,ls.split('-'));z=b[0] if b else a
 assert 1<=a<=z<=len(lines),(fn,ls)
 # Report scan boundary mismatches for human inspection; never alter source text.
 scans=[(i+1,m.group(1)) for i,l in enumerate(lines) if (m:=re.search(r'\\scanpage\{([^}]+)\}',l))]
 current=next((s for i,s in reversed(scans) if i<=a),None)
 assert current==row['scan'],('reading scan mismatch',row['line'],row['scan'],current)
for row in search:
 assert set(row['claim_ids'].split(';'))-{''} <=ci
 for f in row['raw_log'].split('; '):assert (R/'web'/f).exists(),f
assert 'ALL EXECUTED CHECKS PASSED' in (R/'calculation_output.txt').read_text()
for c in claims:
 if 'A^0=k' in c['statement']:assert 'no A^0=k' in c['statement'] or 'not' in c['statement']
counts={'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),'readings':len(readings),'links':len(links),'directions':11,'references':len(refs),'search_rows':len(search),'check_events':len(events),'verdicts':dict(collections.Counter(e['verdict'] for e in entries)),'claim_classes':dict(collections.Counter(c['class'] for c in claims)),'claim_page_statuses':dict(collections.Counter(c['status_on_pages'] for c in claims)),'link_kinds':dict(collections.Counter(l['kind'] for l in links))}
(R/'counts.json').write_text(json.dumps(counts,indent=2)+'\n')
print(json.dumps(counts,indent=2));print('PASS: exact82-entry coverage; required fields; unique IDs; all claims searched; all refs and events resolved; all scan-alarm line ranges/scans verified; code output passed.')
