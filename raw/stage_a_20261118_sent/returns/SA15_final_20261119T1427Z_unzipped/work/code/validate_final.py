"""Structural and provenance-join validation, not mathematical certification."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json,csv,re,hashlib,sys
B=Path(__file__).resolve().parents[2];D=B/'deliverables';W=B/'work'
# The distributed ZIP places deliverables directly at its root.
if not D.exists():D=B
def read(n):return json.loads((D/n).read_text())
def rows(n):return list(csv.DictReader((D/n).open(),delimiter='\t'))
def fail(s):raise AssertionError(s)
required=['SA15_dossier.md','SA15_entries.tsv','SA15_items.json','SA15_claims.json',
 'SA15_problems.json','SA15_readings.tsv','SA15_links.tsv','SA15_directions.md',
 'SA15_references.bib','CHECK_EVENTS.tsv','progress.log']
for n in required:assert (D/n).is_file(),n
schemas={
 'SA15_items.json':'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),
 'SA15_claims.json':'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),
 'SA15_problems.json':'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()}
data={n:read(n) for n in schemas}
for n,required_fields in schemas.items():
 assert isinstance(data[n],list) and data[n]
 for x in data[n]:
  assert set(required_fields)<=x.keys(),(n,x.get('id'),'missing field')
  for k in required_fields:
   assert x[k] is not None,(x['id'],k)
items=data['SA15_items.json'];claims=data['SA15_claims.json'];problems=data['SA15_problems.json']
ii={x['id'] for x in items};cc={x['id'] for x in claims};pp={x['id'] for x in problems}
assert len(ii)==len(items) and len(cc)==len(claims) and len(pp)==len(problems)
assert ii=={f'SA15-{i}' for i in range(1,len(items)+1)}
assert cc=={f'CL-SA15-{i:03}' for i in range(1,len(claims)+1)}
assert pp=={f'MP-SA15-{i:02}' for i in range(1,len(problems)+1)}
allids=ii|cc|pp
for c in claims:
 assert set(c['items'])<=ii and c['items'],c['id']
 assert c['class'] in 'ABCDEF' and len(c['class'])==1
 assert c['confidence'] in ['high','medium','low'],(c['id'],c['confidence'])
 assert c['fate_date']['as_of']=='2026-11-19'
 assert c['statement'] and c['fate'] and c['present_status']
for i in items:
 assert i['check'] in ['agrees','overstates','understates','misreads','not on the page'],(i['id'],i['check'])
 assert i['statement'] and i['check_reason']

entries=rows('SA15_entries.tsv');supp=rows('SA15_supplementary_entries.tsv')
expected=[f'MPL_7_061-072+8_001-078#{i}' for i in range(1,81)]
original=B/'sources/SA15_notes/NOTES_INDEX.tsv'
if original.exists():expected=[x['entry_id'] for x in csv.DictReader(original.open(),delimiter='\t')]
assert [x['entry_id'] for x in entries]==expected
assert len(supp)==847 and len({x['entry_id'] for x in supp})==847
noteids={x['entry_id'] for x in entries+supp}
for e in entries+supp:
 assert e['item_id'] in ii and e['reason'],e
 assert e['verdict'] in ['kept','merged','corrected','withdrawn','rests on a misreading']
for i in items:assert set(i['sources'])<=noteids,(i['id'],i['sources'])
assert set().union(*(set(i['sources']) for i in items))==noteids

evidence=read('SA15_reference_evidence.json');refkeys={x['key'] for x in evidence}
assert len(refkeys)==len(evidence)
for x in evidence:
 assert x['fields']['note'] in ['verified','unverified']
 assert x['fields'].get('title') and x['fields'].get('author'),x['key']
 assert x['inspections']
 if x['fields']['note']=='verified':assert x['fields'].get('url') or x['fields'].get('doi'),x['key']
for x in claims+problems:assert set(x['refs'])<=refkeys,(x['id'],set(x['refs'])-refkeys)
bib=(D/'SA15_references.bib').read_text()
assert set(re.findall(r'@\w+\{([^,]+),',bib))==refkeys

search=rows('SA15_claim_search.tsv')
assert len(search)==len(claims) and {x['claim_id'] for x in search}==cc
assert all(x['search_families'] and x['search_evidence'] and x['exact_fate_assessment'] for x in search)
events=rows('CHECK_EVENTS.tsv');checked={e['statement_id'] for e in events};cb={c['id']:c for c in claims}
assert ii|cc|refkeys<=checked,('missing check events',(ii|cc|refkeys)-checked)
types={'targeted proof check','independent re-proof','computation or formal certificate',
 'used and rechecked in this run','carried as background without fault found',
 "refuted, with the refined statement's id"}
for e in events:
 assert e['type'] in types and all(e.values()),e
 if e['type'].startswith('refuted'):
  targets=set(re.findall(r'CL-SA15-\d+',e['outcome']))
  assert targets and targets<=cc,('missing refined target',e)
  if targets=={e['statement_id']}:
   assert cb[e['statement_id']].get('refined_statement'),('same-record target lacks explicit corrected statement',e)

for name,fields in [('SA15_readings.tsv','cote scan line reading alternative evidence weight confidence'.split()),
 ('SA15_links.tsv',['kind','from','to','what','evidence','note_ids'])]:
 for x in rows(name):assert all(x.get(k) for k in fields),(name,x)
for x in rows('SA15_links.tsv'):assert x['kind'] in ['folder','published work','our projects']
assert not rows('SA15_project_leads.tsv')

for name in ['SA15_dossier.md','SA15_directions.md']:
 text=(D/name).read_text();assert '{{' not in text
 assert not re.search(r'P(?:56|67|78|894)-[ICP]\d{3}',text),('unconverted prose ID',name)
 mentioned=set(re.findall(r'(?<![A-Za-z0-9-])(?:CL-SA15-\d+|MP-SA15-\d+|SA15-\d+)',text))
 assert mentioned<=allids,(name,mentioned-allids)
directions=(D/'SA15_directions.md').read_text()
blocks=re.split(r'(?m)^## \d+\. ',directions)[1:]
assert len(blocks)==12
for b in blocks:
 assert re.search(r'(?<![-A-Za-z])SA15-\d+',b) and 'CL-SA15-' in b and 'MP-SA15-' in b,b[:120]

counts=read('SA15_counts.json')
assert counts['items']==len(items) and counts['claims']==len(claims) and counts['problems']==len(problems)
assert counts['claim_classes']==dict(Counter(x['class'] for x in claims))
assert counts['claim_status_census']==dict(Counter(x['status_census'] for x in claims))
for n,k in [('SA15_readings.tsv','readings'),('SA15_links.tsv','verified_links'),('CHECK_EVENTS.tsv','check_events')]:
 assert len(rows(n))==counts[k],(n,counts[k])
source_check=[]
for x in json.loads((W/'source_inventory.json').read_text()):
 p=B/'sources'/x['path']
 if p.exists():
  assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'],('input changed',p)
  source_check.append(x['path'])
report={'result':'PASS','utc':datetime.now(timezone.utc).isoformat(),
 'meaning':'Structural coverage, source hashes, exact index IDs, references, check events, search joins and prose IDs; not a formal mathematical certificate.',
 'indexed_entries':len(entries),'supplementary_entries':len(supp),'items':len(items),
 'claims':len(claims),'problems':len(problems),'readings':counts['readings'],
 'checked_links':counts['verified_links'],'references':len(refkeys),'check_events':len(events),
 'directions':len(blocks),'source_files_hash_checked':len(source_check),
 'source_hash_qualification':'All 23 supplied files unchanged.' if len(source_check)==23 else 'Original attachments are not all present; available files checked, absent files not claimed checked.'}
(W/'outputs/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
