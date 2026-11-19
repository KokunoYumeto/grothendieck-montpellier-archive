#!/usr/bin/env python3
"""Check proof/register/check-event coverage, recording late separate fragments."""
from pathlib import Path
import csv, json, re, datetime

root = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((root / 'RESEARCH_SA06_results.csv').open()))
events = list(csv.DictReader((root / 'CHECK_EVENTS.tsv').open(), delimiter='\t'))
ids = [row['id'] for row in rows]
checked = {row['statement_id'] for row in events}
seen = set()

def expand(path):
    path = path.resolve()
    if path in seen:
        return ''
    seen.add(path)
    text = path.read_text()
    for name in re.findall(r'\\input\{([^}]+)\}', text):
        target = root / name
        if not target.suffix:
            target = target.with_suffix('.tex')
        text += '\n' + expand(target)
    return text

paper = expand(root / 'RESEARCH_SA06_paper.tex')
numbered = set(re.findall(r'\\paragraph\{([A-F]\.\d+[a-z])\b', paper))
separate = sorted(set(ids) - numbered)
missing_events = sorted(set(ids) - checked)
unregistered = sorted(numbered - set(ids))
missing_paths = []
for row in rows:
    match = re.match(r'([^;\s]+\.tex)', row['where_proved'])
    if match and not (root / match.group(1)).exists():
        missing_paths.append({'id': row['id'], 'path': match.group(1)})
result = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'statement_rows': len(rows),
    'check_events': len(events),
    'unique_ids': len(set(ids)),
    'compiled_numbered_statements': len(numbered),
    'registered_separate_fragments_not_yet_compiled': separate,
    'statements_without_check_events': missing_events,
    'compiled_statements_without_register_rows': unregistered,
    'missing_proof_paths': missing_paths,
    'status': 'pass' if len(ids) == len(set(ids)) and not (
        missing_events or unregistered or missing_paths) else 'fail',
}
out = root / 'logs/register_certificate.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
if result['status'] != 'pass':
    raise SystemExit(1)
