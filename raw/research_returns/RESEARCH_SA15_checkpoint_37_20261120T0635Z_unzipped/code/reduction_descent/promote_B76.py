from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import difflib

own = Path(__file__).resolve().parents[1]
work = own.parents[1]
source = own / 'B_wild_cyclic_point_candidate.tex'
expected = '200539e96e129979c28c346f503143dbd45f9e4b8ebc949cbca0451bb96b9a93'
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == expected
root = json.loads((work / 'outputs/root_B76_audit.json').read_text())
comp = json.loads((own.parent / 'obstructions_crystals/B76_independent_audit.json').read_text())
for audit in (root, comp):
    assert audit['candidate_sha256'] == expected and 'PASS' in audit['status']
preserved = own / 'notes/B_wild_cyclic_point.prepromotion.tex'
assert not preserved.exists()
preserved.write_bytes(raw)
t = re.sub(r'\\status\{Candidate[^}]*\}', lambda _: r'\status{Proved; complete independent root and companion proof and exact-code audits passed.}', raw.decode())
t = t.replace('% Separate post-CP27 candidate. No exact wild-index assertion is inferred.',
              '% Promoted after full root and companion audits; exact wild-index scope is retained.')
needle = 'no executed computation failed.'
assert t.count(needle) == 1
t = t.replace(needle, needle + r'''
The complete independent root and companion proof/code audits
passed; their unchanged-program, author-output-preserving reruns
took \(3.5021978250006214\) and \(3.4459782960038865\) seconds,
respectively. All five assertion records and exact audited
candidate bytes are retained.''')
canonical = own / 'B_wild_cyclic_point.tex'
assert not canonical.exists()
canonical.write_text(t)
labels = re.findall(r'\\label\{([^}]+)\}', t)
assert len(labels) == 5 and r'\status{Candidate' not in t
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'PROVED', 'promotion_utc': now,
    'canonical': str(canonical),
    'canonical_sha256': hashlib.sha256(canonical.read_bytes()).hexdigest(),
    'audited_candidate_sha256': expected,
    'preserved_candidate': str(preserved), 'labels': labels,
    'root_audit': '../../outputs/root_B76_audit.json',
    'root_audit_utc': root['actual_utc'],
    'root_runtime_seconds': root['independent_runtime_seconds'],
    'companion_audit': '../obstructions_crystals/B76_independent_audit.json',
    'companion_audit_utc': comp['actual_utc'],
    'companion_runtime_seconds': comp['elapsed_seconds'],
    'author_runtime_seconds': 3.575578117000987,
    'scope': 'p>=5 with arbitrary absolute ramification e: rational exact p^n in a height2 formal group forces a>(p^2-1)p^(2n-3-v_p(a)); mixed whole/filtered comparison forces e>p^(2n-3-v_p(e)). For mu_p in K, n>=v_p(e)+2 detects total dimension. At p5/e20 any actual125 failure is confined to two whole potentially supersingular groups. No whole-formal125 recovery or exact wild least index is asserted.',
    'source_scope': 'Complete internal B49 and B63 dependencies reread independently; original Hopkins-Gross coefficient/source passages were previously fully audited, without a new external-read claim.',
    'checkpoint_scope': 'Post-CP27 promotion authorized for CP28. Immutable CP27 is unchanged.',
    'executed_failures': []
}
(own / 'outputs/B76_promotion.json').write_text(json.dumps(record, indent=2) + '\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'PROVED_FULL_AUDITS', record['scope'],
                            'B_wild_cyclic_point.tex;outputs/B76_promotion.json',
                            'Root and OC full proof/dependency/code PASS; exact candidate and author output preserved']) + '\n')
with (own / 'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## ' + now + ' — B76 promoted: wild-index cyclic restriction\n\n' + record['scope'] + '\n')

# Parent explicitly authorized these two narrow CP28 wiring changes.
history = own / 'notes/CP28_before_B76_wiring'
assert not history.exists()
history.mkdir()
wiring = []
for rel, old, new in [
    ('code/consolidate.py', "'B_terminal_frobenius_pair.tex']:",
     "'B_terminal_frobenius_pair.tex',\n                    'B_wild_cyclic_point.tex']:"),
    ('code/prepare_checkpoint28.py', "required=['agents/reduction_descent/B_terminal_frobenius_pair.tex']",
     "required=['agents/reduction_descent/B_terminal_frobenius_pair.tex','agents/reduction_descent/B_wild_cyclic_point.tex']")
]:
    path = work / rel
    before = path.read_bytes()
    text = before.decode()
    assert text.count(old) == 1, rel
    updated = text.replace(old, new)
    (history / path.name).write_bytes(before)
    (history / (path.name + '.diff')).write_text(''.join(difflib.unified_diff(
        text.splitlines(True), updated.splitlines(True), fromfile=rel + '.before', tofile=rel)))
    path.write_text(updated)
    wiring.append(dict(path=rel, before_sha256=hashlib.sha256(before).hexdigest(),
                       after_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
wrecord = dict(status='WIRED_NOT_BUILT', actual_utc=datetime.now(timezone.utc).isoformat(),
               canonical_sha256=record['canonical_sha256'], authorized_by='parent explicit message',
               prior_versions=str(history), files=wiring, global_build_executed=False)
(own / 'outputs/B76_CP28_wiring.json').write_text(json.dumps(wrecord, indent=2) + '\n')
print(json.dumps({'promotion': record, 'wiring': wrecord}, indent=2))
