"""Create the separate immutable final ZIP only after research has stopped."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import time
import zipfile
from estimate_archive_size import estimate

root = Path(__file__).resolve().parents[1]
prep = json.loads((root / 'code/output/final_preparation.json').read_text())
review = json.loads((root / f'code/output/formal_review{prep["stopping_review"]}.json').read_text())
assert review['stopping_condition_met'] and review['consecutive_no_movement_reviews'] >= 2
assert json.loads((root / 'code/output/research_stopped.json').read_text())['all_research_agents_stopped']
qa = json.loads((root / 'qa/pdf_verified.json').read_text())
assert hashlib.sha256((root / 'build/RESEARCH_SA12_paper.pdf').read_bytes()).hexdigest() == qa['sha256']
out = root.parent / 'RESEARCH_SA12_final_INCOMPLETE.zip'
assert not out.exists(), 'The final archive is immutable.'
size = estimate(root)
assert size['conservative_bound_bytes'] < 500_000_000, size
(root / 'code/output/final_immediate_size_bound.json').write_text(json.dumps(size, indent=2) + '\n')
shutil.copy2(root / 'build/RESEARCH_SA12_paper.pdf', root / 'RESEARCH_SA12_paper.pdf')
paths = [p for p in sorted(root.rglob('*')) if p.is_file() and p.suffix != '.zip'
         and '__pycache__' not in p.parts and p.name != 'CHECKPOINT_MANIFEST.json']
assert len(paths) < 65_000
created = datetime.now(timezone.utc).isoformat()
start = time.perf_counter()
entries = []
with zipfile.ZipFile(out, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in paths:
        data = p.read_bytes()
        rel = str(p.relative_to(root))
        entries.append({'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
        z.writestr(root.name + '/' + rel, data)
    manifest = dict(kind='separate_final_after_stopping_rule', checkpoint='final', utc=created,
                    stopping_review=prep['stopping_review'], final_status='INCOMPLETE',
                    requested_open=review['requested_open'], files=entries,
                    note='Full current deliverables and research documentation after the required stop. Supplied originals and previous ZIP archives are excluded. All members are hashed from the exact bytes written. This is not an off-cadence checkpoint.')
    data = (json.dumps(manifest, indent=2) + '\n').encode()
    (root / 'CHECKPOINT_MANIFEST.json').write_bytes(data)
    z.writestr(root.name + '/CHECKPOINT_MANIFEST.json', data)
assert out.stat().st_size < 500_000_000, out.stat().st_size
print(json.dumps({'archive': str(out), 'bytes': out.stat().st_size, 'members': len(entries) + 1,
                  'created_utc': created, 'seconds': time.perf_counter() - start}))
