#!/usr/bin/env python3
"""Record an already successful upload; never initiate or repeat an upload."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sys

root = Path(__file__).resolve().parents[1]
n = int(sys.argv[1])
observed = sys.argv[2]
dest = root/f'logs/checkpoint{n:02d}_receipt.json'
if dest.exists():
    raise SystemExit('Checkpoint receipt already exists')
lines = (root/f'logs/checkpoint{n:02d}_upload_stdout.txt').read_text().splitlines()
records = []
for line in lines:
    try:
        parsed = json.loads(line)
    except json.JSONDecodeError:
        continue
    if isinstance(parsed,dict) and 'results' in parsed:
        records.extend(parsed['results'])
matches = [r for r in records if r.get('file_name') == f'RESEARCH_SA20_checkpoint_{n:02d}.zip']
assert len(matches) == 1, matches
record = matches[0]
assert record['status'] == 'succeeded', record
integrity = json.loads((root/f'logs/checkpoint{n:02d}_integrity.json').read_text())
assert integrity['status'] == 'PASS'
record.update({
    'save_observed_utc':observed,
    'receipt_recorded_utc':datetime.now(timezone.utc).isoformat(),
    'bytes':integrity['bytes'], 'files':integrity['files'],
    'sha256':integrity['sha256'],
    'integrity':f"CRC and {integrity['manifest_hashes_checked']} nonself manifest hashes PASS in {integrity['runtime_seconds']} seconds"
})
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
