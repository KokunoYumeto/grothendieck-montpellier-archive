"""Promote only the fully audited detecting-curve lemma; no archive."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
rel = 'parts/D/post23_research/D_finite_puncture_detecting_curve_root.tex'
p = root / rel
old = p.read_bytes()
candidate = hashlib.sha256(old).hexdigest()
assert candidate == '5b550a4ca0368db89ab651ee44020c066e4c3e17194e054a5150820631d46f8a'
audits = {
    'root': 'parts/D/post23_research/audit_detecting_curve_author_root.json',
    'B': 'parts/B/post23_research/audit_root_detecting_curve_B.json',
    'C': 'parts/C/post23_research/audit_root_detecting_curve_C.json',
    'D': 'parts/D/post23_research/audit_detecting_curve_local_types_D.json',
}
for actor, name in audits.items():
    a = json.loads((root / name).read_text())
    assert a['sha256'] == candidate
    assert a.get('verdict', a.get('status', '')).startswith('PASS')
snapshot = p.with_name('detecting_curve_audited.source.txt')
snapshot.write_bytes(old)
changes = [
    ('% Candidate: actual independent audits pending. Not yet assembled.',
     '% Proved after four complete actual-file audits; assembled by root.'),
    ('[Candidate: finite punctures give fixed local types on one curve]',
     '[Proved: finite punctures give fixed local types on one curve]'),
]
new = old.decode()
for before, after in changes:
    assert new.count(before) == 1
    new = new.replace(before, after)
p.write_text(new)
reverse = new
for before, after in reversed(changes):
    reverse = reverse.replace(after, before)
assert reverse.encode() == old
m = dict(recorded_utc=now, promoted_at_utc=now, path=rel,
         sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
         labels=['D:finite-puncture-detecting-curve-local-types'],
         status='Proved',
         audit_scope={actor: 'Complete actual-file PASS; exact scope and source reads in ' + name
                      for actor, name in audits.items()},
         audit_records=audits,
         audited_candidate=dict(path=str(snapshot.relative_to(root)), sha256=candidate),
         promotion=dict(type='Status/comment only', exact_reverse_verified=True, changes=changes),
         scope_precision='One geometric-generic curve detects the original group of a fixed normal proper finite-puncture surface. Local types restrict from fixed original complete local rings; highest classical breaks are uniformly bounded. No assertion about all covers after field extension and no divisorial-boundary extension.',
         movement='Dependency of the finite-puncture global projective and restricted alternating reductions; not an independent movement event.')
(root / 'parts/D/post23_research/integration_manifest_root_detecting_curve.json').write_text(json.dumps(m, indent=2) + '\n')
print(json.dumps({'path': rel, 'sha256': m['sha256'], 'audited_candidate': candidate,
                  'all_four_actual_audits': True, 'archive_created': False}, indent=2))
