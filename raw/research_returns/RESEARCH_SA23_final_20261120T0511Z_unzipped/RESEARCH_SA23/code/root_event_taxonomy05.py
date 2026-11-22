"""Preserve precise event descriptions while using the user's event taxonomy."""
from pathlib import Path
import csv, datetime, hashlib, json, time

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
path = root / 'notes/geometry_CHECK_EVENTS.tsv'
before = path.read_bytes()
with path.open() as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
changes = []
for i, row in enumerate(rows, start=2):
    if row['type'] == 'targeted source check':
        changes.append({'line': i, 'statement_id': row['statement_id'],
                        'old_type': row['type'],
                        'new_type': 'used and rechecked in this run',
                        'original_outcome': row['outcome']})
        row['type'] = 'used and rechecked in this run'
        row['outcome'] = 'Targeted source check (description retained): ' + row['outcome']
if not changes:
    raise SystemExit('No unnormalized source-check events; no file changed.')
with path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'path': str(path.relative_to(root)),
          'sha256_before': hashlib.sha256(before).hexdigest(),
          'sha256_after': hashlib.sha256(path.read_bytes()).hexdigest(),
          'reason': 'The prompt enumerates six event categories. Documentary inspection belongs to used and rechecked in this run; no independent proof is claimed.',
          'changes': changes,
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_event_taxonomy05.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
