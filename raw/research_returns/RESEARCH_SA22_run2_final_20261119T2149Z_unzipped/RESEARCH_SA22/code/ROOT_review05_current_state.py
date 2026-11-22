#!/usr/bin/env python3
"""Check the current metadata at review05; never infer mathematical movement.

The substantive root assessment remains necessary. This program verifies that
the already assessed register, main outcome rows and inspected source build
are still the current files, and records the actual check time.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import json
import time
import zipfile

root = Path(__file__).resolve().parents[1]
started = datetime.now(timezone.utc)
assert started >= datetime(2026, 11, 19, 21, 39, tzinfo=timezone.utc), 'Not yet due; no record written.'
target = root / 'logs/ROOT_review05_current_state.json'
assert not target.exists(), 'Preserve the actual earlier check.'
clock = time.perf_counter()
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def outcomes(text):
    block = text.split('## Outcome table\n', 1)[1].split('\n## ', 1)[0]
    return [line for line in block.splitlines()
            if line.startswith('| ') and not line.startswith('| Item |')]

preliminary = json.loads((root / 'logs/ROOT_review05_preliminary_snapshot.json').read_text())
current_results = root / 'RESEARCH_SA22_results.csv'
assert sha(current_results) == preliminary['current_results_sha256']
rows = list(csv.DictReader(current_results.open()))
assert dict(Counter(r['status'] for r in rows)) == preliminary['current_status_counts']
assert sorted(r['id'] for r in rows if r['status'] == 'Open') == ['U:henselian-comparison']
with zipfile.ZipFile(root.parent / preliminary['baseline_archive']) as archive:
    before = outcomes(archive.read('RESEARCH_SA22/RESEARCH_SA22_report.md').decode('utf-8'))
after = outcomes((root / 'RESEARCH_SA22_report.md').read_text())
assert before == after and len(after) == 45
build = json.loads((root / 'logs/integrated_build_summary.json').read_text())
qa = json.loads((root / 'logs/paper_visual_qa.json').read_text())
assert sha(root / 'RESEARCH_SA22_paper.pdf') == build['pdf_sha256'] == qa['pdf_sha256']
assert qa['inspection'].startswith('PASS')
for name, digest in build['source_hashes_after'].items():
    assert sha(root / name) == digest, 'Changed included source: ' + name
source_resolution = root / 'notes/C_Fujiwara_Crelle433_resolution.md'
assert sha(source_resolution) == '6ce7dd44cdfcbc58bf2d6b2ee908c85a8aad3311edbcc2a15cd6c2bdd5781349'
record = {
    'scope': 'Actual due-time administrative state check; no mathematical certificate or research program rerun; does not record the formal review or authorize a stop',
    'started_utc': started.isoformat(),
    'outcome': 'PASS',
    'statement_count': len(rows),
    'status_counts': dict(Counter(r['status'] for r in rows)),
    'canonical_results_sha256': sha(current_results),
    'unchanged_part_lead_outcome_rows': len(after),
    'current_open_ids': ['U:henselian-comparison'],
    'source_hashes_match_actually_inspected_build': True,
    'build_run_id': build['run_id'],
    'last_concrete_source_route_note': str(source_resolution.relative_to(root)),
    'last_concrete_source_route_sha256': sha(source_resolution),
    'substantive_judgment_required': 'Root must assess the two original-source obligations and every main gate before the formal progress-review command.',
    'elapsed_seconds': time.perf_counter() - clock,
}
with target.open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps(record, indent=2))
