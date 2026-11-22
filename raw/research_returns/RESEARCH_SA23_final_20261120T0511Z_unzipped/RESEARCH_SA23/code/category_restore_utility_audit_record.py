"""Fingerprint the exact restoration utility and README reviewed statically."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
paths = ['code/restore_checkpoint_from_final.py',
         'notes/geometry_final_package_README.md',
         'code/geometry_final_package.py']
record = {'utc': datetime.now(timezone.utc).isoformat(),
          'reviewer': 'GPT-6 Astra, inherited effort, crystalline_categories',
          'kind': 'Independent static code/schema review; no execution of restoration or archive creation',
          'files': [{'path': p, 'bytes': (ROOT/p).stat().st_size,
                     'sha256': hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in paths],
          'finding': 'No concrete defect found for the actual v1 manifest and documented restoration contract'}
output = ROOT / 'logs/category_restore_utility_audit.json'
assert not output.exists(), 'Preserve earlier audit snapshots.'
output.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
