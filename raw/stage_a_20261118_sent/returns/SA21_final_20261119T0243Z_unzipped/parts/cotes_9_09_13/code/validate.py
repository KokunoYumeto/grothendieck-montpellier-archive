"""Integrity checks for authored deliverables, not mathematical proof checking."""
from pathlib import Path
import json,csv,re,datetime,collections
R=Path(__file__).resolve().parents[1]
C=json.loads((R/'claims.json').read_text());P=json.loads((R/'problems.json').read_text())
cf={'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence','status_category','search_ids'}
pf={'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}
allowed={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages','definition/construction','current-run refinement'}
assert len(C)==36 and len(P)==9
assert {c['id'] for c in C}=={f'C-SA21-9-{i:03}' for i in range(31,67)}
assert len({p['id'] for p in P})==len(P)
bib=set(re.findall(r'@\w+\{([^,]+),',(R/'references.bib').read_text()))
assert len(re.findall(r'(?m)^ note = \{verified\},$',(R/'references.bib').read_text()))==len(bib)==6
assert len(re.findall(r'(?m)^ annote = \{',(R/'references.bib').read_text()))==6
with (R/'search_log.tsv').open() as f:S=list(csv.DictReader(f,delimiter='\t'))
sids={s['search_id'] for s in S};assert len(S)==8
for c in C:
 assert cf<=set(c),c['id'];assert c['class'] in 'ABCDEF';assert c['status_category'] in allowed
 assert c['refs'] and set(c['refs'])<=bib,c['id'];assert c['search_ids'] and set(c['search_ids'])<=sids,c['id']
 assert set(c['scans'])<=set(range(66,105)),c['id'];assert 'PENDING' not in str(c)
for p in P:assert pf<=set(p) and p['refs'] and set(p['refs'])<=bib,p['id']
for s in S:assert (R/s['output']).exists(),s['search_id']
def table(name):
 with (R/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))
coverage=table('coverage.tsv');readings=table('readings.tsv');links=table('links.tsv');events=table('check_events.tsv')
assert len(coverage)==5 and len(readings)==16 and len(links)==21
scans=[int(x) for row in coverage for x in row['scan_markers'].split(',')];assert sorted(scans)==list(range(66,105))
eventids={e['statement_id'] for e in events}
assert {c['id'] for c in C}<=eventids;assert bib<=eventids
checks=json.loads((R/'outputs/finite_checks.json').read_text());assert checks['metadata']['all_assertions_passed']
assert checks['hom_has_no_orthocomplement']['all_join_maps_count']==234
assert checks['hom_has_no_orthocomplement']['atoms_count']==40
assert checks['hom_has_no_orthocomplement']['coatoms_count']==16
out={'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'validation':'passed','claims':len(C),'classes':dict(collections.Counter(c['class'] for c in C)),'status_categories':dict(collections.Counter(c['status_category'] for c in C)),'problems':len(P),'folders':len(coverage),'scans':len(scans),'readings':len(readings),'links':len(links),'search_batches':len(S),'check_events':len(events),'references_with_check_event':sorted(bib),'meaning':'Schema, coverage, source/event mapping and saved-certificate integrity only; mathematical evidence remains the cited independent proofs and primary-source checks.'}
(R/'outputs/validation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
with (R/'progress.log').open('a') as f:f.write(out['time_utc']+'\tFinal integrity validation passed; owned IX09–13 artifacts stable.\n')
