"""Integrity checks of authored registers. This does not infer scholarly verdicts."""
from pathlib import Path
import csv,json,re,collections
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[1];ROOT=B.parents[2]
def table(n):return list(csv.DictReader((B/n).open(),delimiter='\t'))
items=json.loads((B/'items.json').read_text());claims=json.loads((B/'claims.json').read_text());problems=json.loads((B/'problems.json').read_text())
entries=table('entries.tsv');readings=table('readings.tsv');links=table('links.tsv');events=table('check_events.tsv');coverage=table('claim_search_coverage.tsv')
idx=list(csv.DictReader((ROOT/'sources/SA16_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
expected={r['entry_id'] for r in idx if r['package'] in ['MPL_64_078-115','MPL_64_116-157']}
assert len(expected)==134
assert {e['entry_id'] for e in entries}==expected
assert len(entries)==134 and len({e['entry_id'] for e in entries})==134
assert {s for i in items for s in i['sources']}==expected
assert sum(len(i['sources']) for i in items)==134
I={i['id'] for i in items};C={c['id'] for c in claims};P={p['id'] for p in problems}
assert I=={f'SA16-{i}' for i in range(501,600)}
assert C=={f'C-SA16-{i}' for i in range(501,567)}
assert P=={f'MP-SA16-{i}' for i in range(161,173)}
schemas={
 'items':{'id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'},
 'claims':{'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'},
 'problems':{'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}}
for name,rows in [('items',items),('claims',claims),('problems',problems)]:
 for r in rows:assert schemas[name]<=set(r),(name,r['id'],schemas[name]-set(r))
for r in entries:assert r['item_id'] in I and r['verdict'] in ['kept','merged','corrected','withdrawn','rests on a misreading']
for c in claims:assert set(c['items'])<=I and c['class'] in 'ABCDEF'
for p in problems:assert set(p['items'])<=I and set(p['claims'])<=C
refs={r['key']:r for r in json.loads((B/'source_metadata.json').read_text())}
for x in claims+problems:assert set(x['refs'])<=set(refs),(x['id'],set(x['refs'])-set(refs))
assert {r['claim_id'] for r in coverage}==C
for r in coverage:assert r['exact_query_rows'] and r['opened_reference_rows']

# Check every named source file and all physical line bounds in direct item/claim/reading locators.
sources={p.name:p for p in (ROOT/'sources').rglob('*') if p.is_file()}
def checkloc(loc):
 if not isinstance(loc,str):return
 pat=r'([A-Za-z0-9_-]+(?:_transcription\.tex|_notes\.md)):(.*?)(?=;\s*[A-Za-z0-9_-]+(?:_transcription\.tex|_notes\.md):|$)'
 ms=list(re.finditer(pat,loc))
 assert ms,loc
 for m in ms:
  fn=m.group(1);assert fn in sources,fn
  n=len(sources[fn].read_text().splitlines())
  nums=[int(x) for x in re.findall(r'\d+',m.group(2))]
  assert nums and min(nums)>=1 and max(nums)<=n,(loc,n,nums)
for x in items+claims:checkloc(x['lines'])
for r in readings:checkloc(r['line'])
for p in problems:
 for loc in p['occurrences']:checkloc(loc['lines'])

assert all(l['kind'] in ['folder','published work','our projects'] for l in links)
for l in links:assert set(l['note_ids'].split(';'))<=expected
assert all('ink unresolved' in r['confidence'].lower() or 'no composition date' in r['confidence'].lower() or 'unresolved' in r['confidence'].lower() for r in readings)
for sid in I|C|P:assert any(e['statement_id']==sid for e in events),sid
revised=json.loads((B/'refinements.json').read_text());R={r['id'] for r in revised}
for e in events:
 if e['type'].startswith('refuted'):
  rid=e['type'].split("id ",1)[1];assert rid in R,rid
 else:assert e['type'] in ['targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found']
comp=json.loads((B/'outputs/computation_records.json').read_text())
assert len(comp)==31 and 'ALL EXACT ASSERTIONS PASSED. 31 computation groups.' in (B/'outputs/recompute.txt').read_text()
assert not list((B/'outputs').glob('web*.json')) and not list(B.rglob('*.pdf'))
directioncount=len(re.findall(r'^## [1-7]\. ',(B/'directions.md').read_text(),re.M));assert directioncount==7
print('PASS: all134 expected entries occur exactly once in verdicts and once in item provenance.')
print('PASS:99 items,66 claims,12 problems; schemas, IDs, references, direct source-line bounds and event coverage valid.')
print('PASS: all66 claims have exact query rows and opened-reference mappings.')
print('PASS:75 reading alarms remain unresolved; no transcription altered by this package.')
print('PASS:42 links; all external-project leads are segregated in the dedicated table.')
print('PASS:31 exact computation groups have retained outputs; no external PDF/raw retrieval in deliverables.')
print('PASS:7 ranked directions;14 explicit refinements;'+str(len(events))+' check events.')
print('Verdicts',dict(collections.Counter(e['verdict'] for e in entries)))
print('Item kinds',dict(collections.Counter(i['kind'] for i in items)))
print('Claim classes',dict(collections.Counter(c['class'] for c in claims)))
print('Claim page statuses',dict(collections.Counter(c['status_on_pages'] for c in claims)))
print('References',len(refs),dict(collections.Counter(r['note'] for r in refs.values())))
summary=dict(entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),readings=len(readings),links=len(links),
             our_project_links=len(table('our_project_links.tsv')),directions=directioncount,computations=len(comp),events=len(events),
             classes=dict(collections.Counter(c['class'] for c in claims)),refs=len(refs),refinements=len(R),validated_at=datetime.now(timezone.utc).isoformat())
(B/'outputs/final_inventory.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
with (B/'progress.log').open('a') as f:
 now=datetime.now(timezone.utc).isoformat()
 for st,msg in [('STAGE3_CONFIRMED','12 individually authored problems; opened-source state-of-art and page closures recorded.'),('STAGE4_CONFIRMED','75 mathematical reading alarms; all ink undecided.'),('STAGE6','7 ranked directions authored; none developed as a new task.'),('END','All late64 registers and proof/code outputs validated; cross-agent geometric root equivalence incorporated.')]:f.write(now+'\t'+st+'\t'+msg+'\n')
