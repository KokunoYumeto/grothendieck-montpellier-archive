"""Validate schemas, identifier/reference closure and recorded source coverage.
This validates documentation integrity, not whether a reading happened; the latter
is recorded by the authored reading ledger and per-entry explanations.
"""
import json,csv,re,collections
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def rows(name):
    with (root/name).open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
items=json.loads((root/'items.json').read_text());claims=json.loads((root/'claims.json').read_text());problems=json.loads((root/'problems.json').read_text())
for name in ['synthesis.md','directions.md','proof_checks.md','primary_reading_Brauer.md','primary_reading_Hartshorne_Katz.md']:
    assert (root/name).stat().st_size>500,name
entries=rows('entries.tsv');readings=rows('readings.tsv');links=rows('links.tsv');events=rows('CHECK_EVENTS.tsv');coverage=rows('reading_coverage.tsv');research=rows('research_log.tsv')
itemfields='id sources kind cote scans lines his_words statement reconstruction check check_reason'.split()
claimfields='id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split()
problemfields='id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()
for objects,fields in [(items,itemfields),(claims,claimfields),(problems,problemfields)]:
    for ob in objects:assert set(ob)==set(fields),(ob['id'],set(ob)^set(fields))
    assert len(objects)==len({ob['id'] for ob in objects})
itemids={x['id'] for x in items};claimids={x['id'] for x in claims}
origins=rows('claim_origins.tsv')
assert len(origins)==len(claims) and {r['claim_id'] for r in origins}==claimids
leads=rows('publication_comparison_leads.tsv')
assert len(leads)==1 and 'NOT a verified' in leads[0]['evidence']
assert not any('EGAIV4 §18.11.6' in r['to'] for r in links)
expected={f'MPL_16+47+54+44#{i}' for i in list(range(1,44))+list(range(80,85))}
assert {x['entry_id'] for x in entries}==expected and len(entries)==48
assert {s for ob in items for s in ob['sources']}==expected
for row in entries:assert row['item_id'] in itemids and len(row['reason'])>25
for c in claims:assert set(c['items'])<=itemids and c['class'] in 'ABCDEF' and c['fate'] and c['statement'] and c['confidence']
for p in problems:
    for occurrence in p['occurrences']:assert set(occurrence['claims'])<=claimids
assert {int(row['scan']) for row in coverage}=={1,*range(3,24),*range(25,57)}
assert len(coverage)==54
bib=(root/'references.bib').read_text()
blocks=re.split(r'(?=@\w+\{)',bib)
refkeys=set()
for block in blocks:
    match=re.match(r'@\w+\{([^,]+),',block)
    if match:
        refkeys.add(match.group(1));assert re.search(r'note\s*=\s*\{(?:verified|unverified)\}',block),match.group(1)
refsused={key for ob in claims+problems for key in ob['refs']}
assert refsused<=refkeys,refsused-refkeys
eventids={x['statement_id'] for x in events}
assert itemids|claimids|refkeys<=eventids,(itemids|claimids|refkeys)-eventids
searchids=set()
for row in research:
    for match in re.finditer(r'CL-SA19-(\d+)(?:[–-](?:CL-SA19-)?(\d+))?',row['claim_ids']):
        lo=int(match.group(1));hi=int(match.group(2) or lo)
        searchids.update(f'CL-SA19-{i}' for i in range(lo,hi+1))
assert claimids<=searchids,claimids-searchids
assert all(row['kind'] in {'folder','published work','our projects'} for row in links)
assert all(row['evidence'] and row['from'] and row['to'] for row in links)
checks=json.loads((root/'outputs/exact_checks.json').read_text())
assert checks['nonzero_norm_not_automatic']['xi_norm']=='0'
assert checks['nonzero_norm_not_automatic']['phi_determinant']=='36/25'
assert checks['six_dimensional_orbit']['Qdet']=='2097152/59049'
report=dict(entries=len(entries),items=len(items),verdicts=dict(collections.Counter(x['verdict'] for x in entries)),claims=len(claims),claims_by_class=dict(sorted(collections.Counter(x['class'] for x in claims).items())),claim_statuses=dict(collections.Counter(x['status_on_pages'] for x in claims)),problems=len(problems),readings=len(readings),links=len(links),link_kinds=dict(collections.Counter(x['kind'] for x in links)),references=len(refkeys),check_events=len(events),research_rows=len(research),covered_scan_markers=len(coverage),exact_computation_sections=len(checks),checked='schema, entry uniqueness/coverage, item/claim/reference/event closure, search-log claim coverage, scan-marker coverage, exact output invariants',not_checked='This script does not certify mathematical truth or perform source reading. Those are individually documented in the records and proofs.')
(root/'outputs/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
print('ALL DOCUMENTATION INTEGRITY CHECKS PASSED.')
