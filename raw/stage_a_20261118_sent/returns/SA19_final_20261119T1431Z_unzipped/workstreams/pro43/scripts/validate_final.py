"""Validate saved identifiers, schemas and coverage without judging mathematics."""
from pathlib import Path
import csv
import hashlib
import json
import re
from collections import Counter

B = Path(__file__).resolve().parents[1]
W = B.parents[1]
def tsv(name):
    with (B/name).open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))
def obj(name):
    return json.loads((B/name).read_text())

required = ['entries.tsv','items.json','claims.json','problems.json','readings.tsv',
            'links.tsv','our_projects.tsv','external_pointer_index.tsv','references.bib',
            'CHECK_EVENTS.tsv','research_log.tsv','reading_coverage.tsv','reading_log.md',
            'synthesis.md','directions.md','computations.md','cross_review.md','progress.log',
            'scripts/calculations.py','outputs/calculations.txt']
assert all((B/p).is_file() and (B/p).stat().st_size for p in required)
schemas = {
 'items.json': 'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),
 'claims.json': 'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),
 'problems.json': 'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split(),
}
data = {p:obj(p) for p in schemas}
for name, fields in schemas.items():
    assert isinstance(data[name],list)
    assert all(set(r)==set(fields) for r in data[name]), name
    assert len({r['id'] for r in data[name]})==len(data[name]), name
items,claims,problems = (data[p] for p in schemas)
itemids={r['id'] for r in items}
claimids={r['id'] for r in claims}
problemids={r['id'] for r in problems}
assert claimids=={f'CL-SA19-{n:03d}' for n in range(1,112)}
assert problemids=={f'MP-SA19-{n:02d}' for n in range(1,40)}
assert all(1<=int(x.split('-')[-1])<=99 for x in itemids)
entries=tsv('entries.tsv')
expected_entries={f'MPL_43_094-142#{n}' for n in range(1,90)}
assert len(entries)==89 and {r['entry_id'] for r in entries}==expected_entries
assert all(r['item_id'] in itemids and r['reason'] for r in entries)
assert {r['verdict'] for r in entries}<={'kept','corrected','merged','withdrawn'}
source_pairs={(s,r['id']) for r in items for s in r['sources']}
assert source_pairs=={(r['entry_id'],r['item_id']) for r in entries}
assert all(set(r['items'])<=itemids for r in claims)
assert all(r['class'] in 'ABCDEF' for r in claims)
refs=set(re.findall(r'^@\w+\{([^,]+),',(B/'references.bib').read_text(),re.M))
assert len(refs)==33
assert all(set(r['refs'])<=refs for r in claims+problems)

index=obj('../../source_audit/page_index.json')
own=[r for r in index if r['file'].endswith('MPL_43_094-142_transcription.tex')]
ownscans={int(r['scan']) for r in own}
assert ownscans==set(range(94,143))-{99,111,127}
assert all(set(r['scans'])<=ownscans for r in items+claims)
readings=tsv('readings.tsv')
assert all(r['cote']=='43' and int(r['scan']) in ownscans for r in readings)
coverage=tsv('reading_coverage.tsv')
assigned=[r for r in coverage if r['purpose']=='assigned full audit']
assert len(assigned)==46 and {int(r['scan']) for r in assigned}==ownscans
page_tuples={(r['cote'],str(r['scan']),r['file'],int(r['line_start']),int(r['line_end'])) for r in index}
assert all((r['cote'],r['scan'],r['source'],int(r['line_start']),int(r['line_end'])) in page_tuples for r in coverage)

links=tsv('links.tsv')
projects=tsv('our_projects.tsv')
pointers=tsv('external_pointer_index.tsv')
assert len(projects)==23 and len(pointers)==160
assert {r['kind'] for r in links}<={'folder','published work','our projects'}
for row in links:
    assert set(filter(None,row['note_ids'].split(';')))<=expected_entries
assert all(r['entry_id'] in expected_entries and 'UNVERIFIED' in r['verification'] for r in pointers)
pointer_pairs={(r['entry_id'],r['target']) for r in pointers}
project_pairs={(e,r['to']) for r in projects for e in r['note_ids'].split(';')}
linked_project_pairs={(e,r['to']) for r in links if r['kind']=='our projects' for e in r['note_ids'].split(';')}
assert pointer_pairs==project_pairs==linked_project_pairs
assert all('UNVERIFIED' in r['evidence'] for r in projects)

events=tsv('CHECK_EVENTS.tsv')
eventids={r['statement_id'] for r in events}
assert itemids|claimids|problemids|refs<=eventids
assert all(r['date']=='2026-11-19' and r['who'] and r['type'] and r['outcome'] for r in events)
research=tsv('research_log.tsv')
assert claimids<={r['claim_ids'] for r in research}
sections={int(n) for n in re.findall(r'^## (\d+)\.',(B/'computations.md').read_text(),re.M)}
assert sections==set(range(1,25))
for row in claims:
    for n in re.findall(r'computations\.md §(\d+)',row['computation']):
        assert int(n) in sections
assert 'All finite assertions passed.' in (B/'outputs/calculations.txt').read_text()

manifest=obj('../../source_audit/source_manifest.json')
checked_sources=[]
for row in manifest:
    if 'MPL_43_094-142' in row['file']:
        source=W.parent/'source'/row['file']
        assert source.is_file(), source
        assert hashlib.sha256(source.read_bytes()).hexdigest()==row['sha256'], source
        checked_sources.append(row['file'])
assert checked_sources
counts=obj('outputs/audit_counts.json')
assert counts['entries']==len(entries)==89
assert counts['items']==len(items)==80
assert counts['claims']==len(claims)==111
assert counts['problems']==len(problems)==39
assert counts['readings']==len(readings)==57
assert counts['links']==len(links)==71
assert counts['references']==len(refs)==33
assert counts['check_events']==len(events)
assert counts['research_rows']==len(research)==113
assert counts['verdicts']==dict(Counter(r['verdict'] for r in entries))
assert counts['claim_classes']==dict(Counter(r['class'] for r in claims))
report={'result':'PASS','entries':len(entries),'items':len(items),'claims':len(claims),
        'problems':len(problems),'readings':len(readings),'links':len(links),
        'external_targets':len(projects),'external_entry_target_pairs':len(pointers),
        'references':len(refs),'check_events':len(events),'research_rows':len(research),
        'assigned_faces_read':len(assigned),'all_faces_read':len(coverage),
        'unchanged_source_hashes':checked_sources,
        'verification_boundary':'Structural checks do not replace the recorded full reading or constitute mathematical proof.'}
(B/'outputs/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
