"""Schema/coverage validation, separate from the manual mathematical review."""
import json,csv,re
from pathlib import Path
O=Path(__file__).resolve().parents[1]
schemas={
 'items.json':'id sources kind cote scans lines his_words statement reconstruction check check_reason',
 'claims.json':'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence',
 'problems.json':'id title occurrences as_he_states plausible_today state_of_art why_open worth refs',
}
D={}
for file,fields in schemas.items():
 a=json.loads((O/file).read_text());D[file]=a
 assert len({x['id'] for x in a})==len(a),file
 for x in a: assert set(x)==set(fields.split()),(file,x['id'],set(x)^set(fields.split()))
 print(file,len(a),'records; exact schema and unique ids PASS')
items={x['id'] for x in D['items.json']};claims={x['id'] for x in D['claims.json']}
refs={x['key'] for x in json.loads((O/'REFERENCE_ACCESS.json').read_text())}
for c in D['claims.json']:
 assert set(c['items'])<=items,(c['id'],'items')
 assert set(c['refs'])<=refs,(c['id'],'refs')
for p in D['problems.json']: assert set(p['refs'])<=refs,(p['id'],'refs')
S=json.loads((O/'CLAIM_SEARCH_MAP.json').read_text());assert {x['claim_id'] for x in S}==claims
for s in S:
 assert s['search_files'],s['claim_id']
 for file in s['search_files']:assert (O/file).exists(),file
E=list(csv.DictReader((O/'entries.tsv').open(),delimiter='\t'))
assert len(E)==91 and {x['entry_id'] for x in E}=={f'MPL_33_002-049#{n}' for n in range(1,92)}
assert {x['item_id'] for x in E}<=items
for x in D['items.json']:
 for sid in x['sources']:assert any(r['entry_id']==sid and r['item_id']==x['id'] for r in E)
for filename,heads in [('readings.tsv','cote scan line reading alternative evidence weight confidence'),('links.tsv','kind from to what evidence note_ids'),('CHECK_EVENTS.tsv','statement_id date who type outcome')]:
 with (O/filename).open() as f:
  r=csv.DictReader(f,delimiter='\t');assert r.fieldnames==heads.split(),filename
  rows=list(r);assert all(None not in x for x in rows),filename
  print(filename,len(rows),'rows; schema PASS')
events=list(csv.DictReader((O/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
assert items|claims|refs <= {r['statement_id'] for r in events}
assert 'ALL EXACT ASSERTIONS PASSED' in (O/'outputs/exact_checks.txt').read_text()
assert 'Formal-group quadratic calculation' in (O/'outputs/exact_checks.txt').read_text()
assert {r['scan'] for r in csv.DictReader((O/'SOURCE_COVERAGE.tsv').open(),delimiter='\t')}=={str(n) for n in range(2,50)}
for file in ['review.md','directions.md','references.bib','READ_LOG.tsv','SEARCH_LOG.md','progress.log']:assert (O/file).stat().st_size>0,file
print('All91 entry verdicts linked; all79 claim fates searched; all items/claims/references have check events.')
print('Full48-scan coverage index and saved exact-program completion PASS. Validation is structural, not a substitute for reading or proof.')
