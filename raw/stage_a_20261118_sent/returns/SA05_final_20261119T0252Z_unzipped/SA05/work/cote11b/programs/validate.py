"""Structural audit of the completed manually authored contribution.
This script validates coverage and referential integrity, not mathematical truth.
"""
from pathlib import Path
import json,csv,re,hashlib,collections

base=Path('SA05/work/cote11b')
def js(n):return json.loads((base/n).read_text())
def ts(n):return list(csv.DictReader((base/n).open(),delimiter='\t'))
items=js('items.json');claims=js('claims.json');problems=js('problems.json')
entries=ts('entries.tsv');readings=ts('readings.tsv');links=ts('links.tsv')
events=ts('CHECK_EVENTS.tsv');searches=ts('search_log.tsv');refs=ts('reference_checks.tsv')
req={
 'items':set('id sources kind cote scans lines his_words statement reconstruction check check_reason'.split()),
 'claims':set('id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split()),
 'problems':set('id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split())}
for name,data in [('items',items),('claims',claims),('problems',problems)]:
 assert len({x['id'] for x in data})==len(data),name
 for x in data:assert req[name]<=x.keys(),(name,x['id'],req[name]-x.keys())
expected={r['entry_id'] for r in csv.DictReader(open('sources/notes/NOTES_INDEX.tsv'),delimiter='\t') if r['entry_id'].startswith('MPL_11_043-058+56#')}
assert len(expected)==107
assert {x['entry_id'] for x in entries}==expected and len(entries)==107
ii={x['id']:x for x in items};cc={x['id']:x for x in claims};rr={x['key']:x for x in refs}
assert len(rr)==len(refs)
for e in entries:
 assert e['item_id'] in ii and e['entry_id'] in ii[e['item_id']]['sources'],e
 assert e['verdict'] in ['kept','merged','corrected','withdrawn','rests on a misreading']
for x in items:
 assert all(s in expected for s in x['sources']),x['id']
 assert x['check'] in ['agrees','overstates','understates','misreads','not on the page']
for x in claims:
 assert all(y in ii for y in x['items']),x['id']
 assert set(x['refs'])<=rr.keys(),(x['id'],set(x['refs'])-rr.keys())
 assert x['class'] in 'ABCDEF' and len(x['class'])==1
 assert '2026-11-19' in x['present_status']
for x in problems:
 assert set(x['refs'])<=rr.keys(),x['id']
 assert all(y in cc for y in x.get('claims',[])),x['id']
assert len(searches)==len(claims) and {x['claim_id'] for x in searches}==cc.keys()
assert all(x['queries'] and x['venues'] and x['outcome'] and x['checked_extent'] for x in searches)
assert all(x['kind'] in ['folder','published work'] for x in links)
allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
assert all(x['type'] in allowed for x in events)
event_ids={x['statement_id'] for x in events}
assert set(ii)|set(cc)|set(rr)<=event_ids
for x in claims:
 if x['status_on_pages']=='false as stated':
  assert any(y['statement_id']==x['id'] and y['type'].startswith('refuted') for y in events),x['id']
assert all(x['note'] in ['verified','unverified'] for x in refs)
bib=(base/'references.bib').read_text()
for k,r in rr.items():
 assert '{'+k+',' in bib,k
 assert r['checked_extent'] and r['verification_level'],k

# Check every actual source locator against a real file and valid physical lines.
checked_locs=[]
def locator(s):
 m=re.fullmatch(r'(sources/[^:]+):(\d+(?:-\d+)?(?:,\d+(?:-\d+)?)*)',s)
 if not m:return
 p=Path(m.group(1));assert p.exists(),s
 n=len(p.read_text().splitlines())
 for part in m.group(2).split(','):
  a,*rest=part.split('-');a=int(a);b=int(rest[0]) if rest else a
  assert 1<=a<=b<=n,(s,n)
 checked_locs.append(s)
for x in items+claims:
 for l in x['lines']:locator(l)
for x in problems:
 for o in x['occurrences']:locator(o['lines'])
for x in readings:locator(x['line'])
for x in links:
 for k in ['from','to']:
  for s in re.findall(r'sources/[^; ]+:\d+(?:[-,]\d+)*',x[k]):locator(s)

# Confirm the full-file reading records refer to unchanged source bytes.
reading_records=ts('reading_log.tsv')
for row in reading_records:
 p=Path(row['file']);assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['file']
assert len([x for x in reading_records if x['file'].startswith('sources/')])>=10

checks=js('outputs/checks.json')
assert len(checks)==16
for p in ['programs/build.py','programs/complete.py','programs/checks.py','programs/reading_ledger.py','programs/acquire_references.py','programs/render_references.py','outputs/checks_run.txt','outputs/proof_notes.md','outputs/reference_acquisition.json','outputs/reference_rendering.json','directions.md','overview.md']:
 assert (base/p).is_file(),p
for p in base.rglob('*'):
 if p.is_file():assert p.suffix.lower() not in ['.pdf','.png','.jpg','.jpeg'],p
counts=js('outputs/counts.json')
actual=dict(entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),readings=len(readings),checked_links=len(links),external_leads=len(ts('our_projects_links.tsv'))+len(ts('unverified_link_leads.tsv')),references=len(refs),searches=len(searches),events=len(events))
for k,v in actual.items():assert counts[k]==v,(k,v,counts[k])
result=dict(status='passed',date='2026-11-19',counts=actual,source_locators_checked=len(checked_locs),reading_records_unchanged=len(reading_records),computation_families=len(checks),verdicts=dict(collections.Counter(x['verdict'] for x in entries)),classes=dict(collections.Counter(x['class'] for x in claims)),limits='Coverage, schema, references, unchanged source hashes and saved execution outputs checked. This validation does not infer mathematical truth or certify a reading of unseen images.')
(base/'outputs/validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
