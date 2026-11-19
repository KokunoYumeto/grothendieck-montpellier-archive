"""Read-only structural audit of the consolidated SA05 tables.

Output is a set of candidates and integrity checks. Mathematical judgment is
recorded separately by the reviewer after reading the actual record fields.
"""
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]
OUT = BASE / 'work' / 'cote11b' / 'outputs'
names = ['SA05_items.json', 'SA05_claims.json', 'SA05_problems.json',
         'SA05_entries.tsv', 'SA05_readings.tsv', 'SA05_links.tsv',
         'SA05_project_leads.tsv', 'SA05_unavailable_archive_leads.tsv',
         'CHECK_EVENTS.tsv', 'SA05_aliases.json', 'counts.json']
raw = {name: (BASE / name).read_bytes() for name in names}
data = {}
for name, blob in raw.items():
    text = blob.decode()
    data[name] = json.loads(text) if name.endswith('.json') else list(
        csv.DictReader(text.splitlines(), delimiter='\t'))
items, claims, problems = (data[f'SA05_{k}.json'] for k in ['items','claims','problems'])
ids = {k: {x['id'] for x in v} for k, v in
       [('items',items),('claims',claims),('problems',problems)]}
all_ids = set().union(*ids.values())
entries = data['SA05_entries.tsv']
entry_ids = {x['entry_id'] for x in entries}
index_path = BASE.parent / 'sources' / 'notes' / 'NOTES_INDEX.tsv'
with index_path.open() as f:
    source_index = list(csv.DictReader(f, delimiter='\t'))
index_field = 'entry_id' if 'entry_id' in source_index[0] else 'id'
expected_entries = {x[index_field] for x in source_index}
issues = []
for k, values in [('items',items),('claims',claims),('problems',problems)]:
    duplicates = [x for x,n in Counter(x['id'] for x in values).items() if n>1]
    if duplicates: issues.append({'type':'duplicate_ids','table':k,'ids':duplicates})
if entry_ids != expected_entries:
    issues.append({'type':'entry_coverage','missing':sorted(expected_entries-entry_ids),
                   'unexpected':sorted(entry_ids-expected_entries)})
if len(entries) != len(entry_ids): issues.append({'type':'duplicate_entry_rows'})
for entry in entries:
    if entry['item_id'] not in ids['items']:
        issues.append({'type':'dangling_entry_item','entry':entry})
for item in items:
    for entry in item['sources']:
        if entry not in entry_ids:
            issues.append({'type':'unknown_item_source','item':item['id'],'source':entry})
for claim in claims:
    for item in claim['items']:
        if item not in ids['items']:
            issues.append({'type':'dangling_claim_item','claim':claim['id'],'item':item})
for problem in problems:
    for claim in problem.get('claims', problem.get('claim_ids', [])):
        if claim not in ids['claims']:
            issues.append({'type':'dangling_problem_claim','problem':problem['id'],'claim':claim})
    for occurrence in problem.get('occurrences',[]):
        if isinstance(occurrence,dict) and occurrence.get('item') and occurrence['item'] not in ids['items']:
            issues.append({'type':'dangling_occurrence_item','problem':problem['id'],'item':occurrence['item']})

aliases = data['SA05_aliases.json']
for kind in ['items','claims','problems']:
    for old,new in aliases[kind].items():
        if old in ids[kind] or new not in ids[kind]:
            issues.append({'type':'alias_integrity','kind':kind,'old':old,'new':new})

events = data['CHECK_EVENTS.tsv']
events_by_id = defaultdict(list)
for n,event in enumerate(events,2):
    events_by_id[event['statement_id']].append(event)
    if re.fullmatch(r'(?:MP-)?SA05-(?:C)?\d+',event['statement_id']) and event['statement_id'] not in all_ids:
        issues.append({'type':'dangling_event_statement','physical_line':n,'event':event})

missing_events = {kind:sorted(values-set(events_by_id)) for kind,values in ids.items()}
refutations = []
for n,event in enumerate(events,2):
    if 'refuted' in event['type']:
        targets = re.findall(r'SA05-C\d+(?:\.statement)?',event['outcome'])
        targets = list(dict.fromkeys(targets))
        refutations.append({'line':n,'subject':event['statement_id'],
                            'targets':targets,'target_exists_as_claim':[t in ids['claims'] for t in targets],
                            'self_targets':[t for t in targets if t.removesuffix('.statement')==event['statement_id']],
                            'outcome':event['outcome']})

false_claims = []
for claim in claims:
    if 'false' in claim.get('status_on_pages',''):
        false_claims.append({'id':claim['id'],'status':claim['status_on_pages'],
                             'refined_statement':claim.get('refined_statement'),
                             'refutation_events':sum('refuted' in x['type'] for x in events_by_id[claim['id']])})

lead_patterns = re.compile(r'not attached|not supplied|unavailable|unverified|absent|unchecked|lead|metadata only',re.I)
link_candidates = []
for n,row in enumerate(data['SA05_links.tsv'],2):
    if lead_patterns.search(' '.join(row.values())):
        link_candidates.append({'line':n,**row})

result = {
    'snapshot_utc':datetime.now(timezone.utc).isoformat(),
    'hashes':{name:hashlib.sha256(blob).hexdigest() for name,blob in raw.items()},
    'counts':{name:len(value) for name,value in data.items() if isinstance(value,list)},
    'structural_issues':issues,
    'missing_check_events':missing_events,
    'false_claims':false_claims,
    'refutation_targets':refutations,
    'links_requiring_manual_review':link_candidates,
    'link_kind_counts':dict(Counter(x['kind'] for x in data['SA05_links.tsv'])),
    'known_exclusions':'Reference aliases and merged-into spelling normalization are outside this audit.',
    'limitation':'Scripts expose candidates and validate links/IDs. They do not infer mathematical correctness or source reading.',
}
output_name = sys.argv[1] if len(sys.argv)>1 else 'consolidated_structure_audit.json'
assert Path(output_name).name == output_name, 'Use a filename within the audit output directory.'
(OUT/output_name).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['snapshot_utc','counts','structural_issues','missing_check_events','link_kind_counts']},ensure_ascii=False,indent=2))
print('False-status claims:',len(false_claims),'refutation events:',len(refutations),'link review candidates:',len(link_candidates))
