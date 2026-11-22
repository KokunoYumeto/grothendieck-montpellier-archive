"""Freeze the assembled CP30 manuscript sources after the final clean build."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
build = sys.argv[1]
run = json.loads((root / f'code/output/{build}.run.json').read_text())
log = (root / f'code/output/{build}.stdout.txt').read_text()
assert run['returncode'] == 0
assert not any(word in log for word in ['Warning', 'Missing character', 'undefined'])
over = [float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)', log)]
assert max(over, default=0) <= 2
prior = json.loads((root / 'code/output/checkpoint29_source_freeze.json').read_text())
paths = set(prior['files'])
for p in (root / 'code/output').glob('integrate_post19_post29*.json'):
    paths.update(x['path'] for x in json.loads(p.read_text())['files'])
with (root / 'RESEARCH_SA12_results.csv').open() as f:
    rows = list(csv.DictReader(f))
with (root / 'CHECK_EVENTS.tsv').open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
assert len(rows) == 487 and len(events) == 1655
correction = json.loads((root / 'code/output/integrate_A_chain_coordinate_correction.json').read_text())
assert hashlib.sha256((root / correction['integrated_path']).read_bytes()).hexdigest() == correction['integrated_sha256']
record = {'utc': datetime.now(timezone.utc).isoformat(), 'checkpoint': 30,
          'scheduled_utc': '2026-11-20T22:40:00+00:00', 'build': build,
          'statement_count': len(rows), 'check_event_count': len(events),
          'requested_outcomes': 57,
          'files': {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in sorted(paths)},
          'archive_created': False,
          'coordinate_correction': 'code/output/integrate_A_chain_coordinate_correction.json',
          'note': 'The five auxiliary units and the fully audited intrinsic A-chain coordinate correction are assembled. The earlier erroneous source, exact delta and all prior QA records are preserved. Separate research may continue; no further manuscript integration before checkpoint30 unless a correctness defect requires repair.'}
out = root / 'code/output/checkpoint30_source_freeze.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'build': build, 'frozen_sources': len(paths), 'statements': len(rows),
                  'check_events': len(events), 'maximum_overfull_pt': max(over, default=0)}))
