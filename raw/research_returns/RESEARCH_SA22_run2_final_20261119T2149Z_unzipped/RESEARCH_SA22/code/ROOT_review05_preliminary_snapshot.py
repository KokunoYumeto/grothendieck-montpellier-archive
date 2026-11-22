#!/usr/bin/env python3
"""Record current register differences for a later substantive root review.

This is an administrative comparison, not a formal progress review or a
mathematical verification. It neither decides movement nor authorizes stopping.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import json
import time
import zipfile

root = Path(__file__).resolve().parents[1]
target = root / 'logs/ROOT_review05_preliminary_snapshot.json'
assert not target.exists(), 'Preserve the earlier snapshot; do not overwrite it.'
started = datetime.now(timezone.utc)
clock = time.perf_counter()
baseline = root.parent / 'RESEARCH_SA22_checkpoint_08.zip'
def sha(data):
    return hashlib.sha256(data).hexdigest()
def rows(data):
    return list(csv.DictReader(io.StringIO(data.decode('utf-8'))))
def outcome_rows(text):
    section = text.split('## Outcome table\n', 1)[1].split('\n## ', 1)[0]
    return [line for line in section.splitlines()
            if line.startswith('| ') and not line.startswith('| Item |')]

with zipfile.ZipFile(baseline) as archive:
    old_csv = archive.read('RESEARCH_SA22/RESEARCH_SA22_results.csv')
    old_report = archive.read('RESEARCH_SA22/RESEARCH_SA22_report.md')
    old_review = archive.read('RESEARCH_SA22/logs/progress_review_04.json')
current_csv = (root / 'RESEARCH_SA22_results.csv').read_bytes()
current_report = (root / 'RESEARCH_SA22_report.md').read_bytes()
old = {r['id']: r for r in rows(old_csv)}
current = {r['id']: r for r in rows(current_csv)}
old_outcomes = outcome_rows(old_report.decode('utf-8'))
current_outcomes = outcome_rows(current_report.decode('utf-8'))
record = {
    'scope': 'Read-only comparison of current canonical status fields and Part/Lead outcome rows to checkpoint08; no theorem or certificate rerun',
    'started_utc': started.isoformat(),
    'baseline_archive': baseline.name,
    'baseline_review_04': json.loads(old_review),
    'baseline_results_sha256': sha(old_csv),
    'current_results_sha256': sha(current_csv),
    'baseline_report_sha256': sha(old_report),
    'current_report_sha256': sha(current_report),
    'baseline_statement_count': len(old),
    'current_statement_count': len(current),
    'new_statement_ids': sorted(set(current) - set(old)),
    'removed_statement_ids': sorted(set(old) - set(current)),
    'changed_statuses': [
        {'id': key, 'before': old[key]['status'], 'after': current[key]['status']}
        for key in sorted(set(old) & set(current))
        if old[key]['status'] != current[key]['status']
    ],
    'baseline_open_ids': sorted(k for k, r in old.items() if r['status'] == 'Open'),
    'current_open_ids': sorted(k for k, r in current.items() if r['status'] == 'Open'),
    'current_status_counts': dict(Counter(r['status'] for r in current.values())),
    'baseline_outcome_rows': len(old_outcomes),
    'current_outcome_rows': len(current_outcomes),
    'part_lead_outcomes_byte_equal': old_outcomes == current_outcomes,
    'outcome_rows_only_in_baseline': [r for r in old_outcomes if r not in current_outcomes],
    'outcome_rows_only_in_current': [r for r in current_outcomes if r not in old_outcomes],
    'formal_review_recorded': False,
    'limitation': 'A substantive root assessment must determine whether any new proof strictly reduces a main gate. This snapshot cannot make that mathematical judgment and cannot substitute for the actual scheduled review.',
    'elapsed_seconds': time.perf_counter() - clock,
}
with target.open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps(record, indent=2))
