"""Verify every original and consolidated program/output catalog checksum.

The catalog cannot contain its own checksum. FILE_LIST.tsv in the immutable
archive supplies the checksum of the catalog itself.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
records = json.loads((root / 'code/program_files_output.json').read_text())
failures = []
assert not any(r['original'] == 'code/program_files_output.json' for r in records)
for record in records:
    for field in ('original', 'collected'):
        path = root / record[field]
        if not path.is_file():
            failures.append({'field': field, 'path': str(path), 'error': 'missing'})
            continue
        data = path.read_bytes()
        if len(data) != record['bytes'] or hashlib.sha256(data).hexdigest() != record['sha256']:
            failures.append({'field': field, 'path': str(path), 'error': 'size/hash mismatch'})
result = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'status': 'pass' if not failures else 'fail',
    'records_checked': len(records),
    'failures': failures,
    'self_checksum': 'deliberately excluded; supplied by immutable archive manifest',
    'runtime_seconds': time.perf_counter() - started,
}
(root / 'logs/program_catalog_verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
if failures:
    raise SystemExit(1)
