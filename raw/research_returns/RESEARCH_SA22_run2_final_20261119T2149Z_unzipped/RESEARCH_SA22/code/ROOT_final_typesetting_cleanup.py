#!/usr/bin/env python3
"""Apply two formatting corrections after the required research stop.

The unit notation keeps the same meaning and no statement, proof argument,
status or label is changed. The earlier source bytes and pending render
record are preserved. A new build and actual image inspection remain required.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time

root = Path(__file__).resolve().parents[1]
started = datetime.now(timezone.utc)
clock = time.perf_counter()
status = json.loads((root / 'logs/final_status.json').read_text())
assert status['status'] == 'INCOMPLETE'
assert datetime.fromisoformat(status['research_stopped_utc']) <= started
history = root / 'notes/final_typography_before'
assert not history.exists(), 'Preserve the original formatting snapshot.'
changes = {
    'notes/C_KnudsenMumford_sign_fragment.tex':
        ('\\boldsymbol 1=(\\mathcal O_S,0).', '\\symbf{1}=(\\mathcal O_S,0).'),
    'sections/A2a_projective.tex':
        ('\\subsubsection{A.2(a): a cap cannot depend only on its own length}',
         '\\subsection{A.2(a): a cap cannot depend only on its own length}'),
}
def sha(data):
    return hashlib.sha256(data).hexdigest()
prepared = {}
for name, (old, new) in changes.items():
    original = (root / name).read_bytes()
    text = original.decode('utf-8')
    assert text.count(old) == 1
    prepared[name] = (original, text.replace(old, new, 1).encode('utf-8'))
pending_path = root / 'logs/paper_visual_qa_pending.json'
pending = json.loads(pending_path.read_text())
assert pending['run_id'] == '20261119T213921Z'
assert pending['inspection'].startswith('PENDING')
pending_archive = root / 'logs/visual_qa_runs/20261119T213921Z_not_approved.json'
assert not pending_archive.exists()
pending_archive.write_bytes(pending_path.read_bytes())
history.mkdir()
for name, (before, after) in prepared.items():
    backup = history / name
    backup.parent.mkdir(parents=True, exist_ok=True)
    backup.write_bytes(before)
    (root / name).write_bytes(after)
record = {
    'started_utc': started.isoformat(),
    'scope': 'Publication formatting after the required research stop; no mathematical statement, label, status, certificate or proof argument changed',
    'changes': [
        'Use the Unicode mathematics bold digit for the already defined tensor unit, removing the unavailable bold-font-shape fallback requested by boldsymbol.',
        'Use a subsection for the first A.2(a) heading directly beneath its section, removing a skipped bookmark level; theorem counters remain section-based.',
    ],
    'files': [{'path': name, 'before_sha256': sha(before), 'after_sha256': sha(after)}
              for name, (before, after) in prepared.items()],
    'prior_pending_render_record': str(pending_archive.relative_to(root)),
    'prior_pending_run_actually_approved': False,
    'publication_state': 'New compilation and actual visual inspection required.',
    'elapsed_seconds': time.perf_counter() - clock,
}
(root / 'logs/ROOT_final_typesetting_cleanup.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
