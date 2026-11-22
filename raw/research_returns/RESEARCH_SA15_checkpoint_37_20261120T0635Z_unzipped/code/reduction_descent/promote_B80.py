from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, difflib

own = Path(__file__).resolve().parents[1]
work = own.parents[1]
candidate = own / 'B_first_wild_fourth_layer_candidate.tex'
raw = candidate.read_bytes()
expected = 'fc7d5bf4a947feb60de702f1d16c7432a8fddd6480f6f42f9dff7317f21f386e'
assert hashlib.sha256(raw).hexdigest() == expected
root = json.loads((work / 'outputs/root_B80_audit.json').read_text())
oc = json.loads((own.parent / 'obstructions_crystals/B80_independent_audit.json').read_text())
for audit in (root, oc):
    assert audit['candidate_sha256'] == expected and 'PASS' in audit['status']
pre = own / 'notes/B_first_wild_fourth_layer.prepromotion.tex'
assert not pre.exists()
pre.write_bytes(raw)
s = re.sub(r'\\status\{Candidate[^}]*\}', lambda _: r'\status{Proved; full independent root and companion proof and exact-code audits passed.}', raw.decode())
s = s.replace('% Separate post-CP28 candidate; the final abelian-image branch remains unresolved.',
              '% Proved after complete independent audits; the final abelian-image branch remains unresolved.')
needle = 'all-prime argument and establish no BT-group existence.'
assert s.count(needle) == 1
s = s.replace(needle, needle + r'''

The independent root and companion audits read the entire final proof
and certificate and reread the actual B79, B57 and B60 dependency
arguments. Their unchanged isolated reruns passed in
\(0.983579940002528\) and \(1.0418004910025047\) seconds,
respectively, preserving the author output. These audits make no
additional fresh original-source claim. The exact audited candidate,
initial and corrected programs and outputs, and the withdrawn
orbit-rank shortcut remain retained with the promotion record.''')
canonical = own / 'B_first_wild_fourth_layer.tex'
assert not canonical.exists()
canonical.write_text(s)
labels = re.findall(r'\\label\{([^}]+)\}', s)
assert labels == root['labels'] == oc['labels'] and len(labels) == 6
assert r'\status{Candidate' not in s
now = datetime.now(timezone.utc).isoformat()
scope = ('At e=p(p-1), a different-special-character actual p^3 pair with irreducible residual inertia '
         'and wild image of order p^4 has abelian full finite image, with wild image equal to the '
         'principal units of a rank-one unramified-quadratic algebra modulo p^3. '
         'This is finite-level only: no whole-group CM, branch existence/exclusion, larger-image '
         'or reducible-residual conclusion is inferred.')
record = {
    'status': 'PROVED', 'promotion_utc': now,
    'canonical': str(canonical),
    'canonical_sha256': hashlib.sha256(canonical.read_bytes()).hexdigest(),
    'audited_candidate_sha256': expected, 'preserved_candidate': str(pre),
    'labels': labels, 'root_audit': '../../outputs/root_B80_audit.json',
    'root_audit_utc': root['actual_utc'],
    'root_runtime_seconds': root['independent_runtime_seconds'],
    'companion_audit': '../obstructions_crystals/B80_independent_audit.json',
    'companion_audit_utc': oc['actual_utc'],
    'companion_runtime_seconds': oc['independent_runtime_seconds'],
    'author_runtime_seconds': 0.9882168779877247, 'scope': scope,
    'source_scope': 'Full internal B79/B57/B60 dependency proofs reread; no new original-source read claimed.',
    'retained_corrections': ['notes/B79_next_wild_routes.before_orbit_gap.md',
                             'outputs/B79_exploratory_orbit_gap.json',
                             'notes/B_first_wild_fourth_layer.before_anti_scalar.tex',
                             'notes/B80_initial_certificate'],
    'checkpoint_scope': 'CP29; immutable CP28 unchanged.', 'executed_failures': []}
(own / 'outputs/B80_promotion.json').write_text(json.dumps(record, indent=2) + '\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'PROVED_FULL_AUDITS', scope,
                           'B_first_wild_fourth_layer.tex;outputs/B80_promotion.json',
                           'Full root+OC proof/code audits; candidate and corrected outputs retained']) + '\n')
with (own / 'STATUS_CURRENT.md').open('a') as f:
    f.write('\n## ' + now + ' — B80 promoted: finite Cartan fourth layer\n\n' + scope + '\n')

history = own / 'notes/CP29_before_B80_wiring'
assert not history.exists()
history.mkdir()
edits = [
    (work / 'code/consolidate.py', "'B_first_wild_irreducible_image.tex']:",
     "'B_first_wild_irreducible_image.tex',\n                    'B_first_wild_fourth_layer.tex']:"),
    (work / 'code/prepare_checkpoint29.py',
     "required=['agents/reduction_descent/B_first_wild_irreducible_image.tex',",
     "required=['agents/reduction_descent/B_first_wild_irreducible_image.tex',\n          'agents/reduction_descent/B_first_wild_fourth_layer.tex',")]
wiring = []
for path, old, new in edits:
    before = path.read_bytes()
    text = before.decode()
    assert text.count(old) == 1
    after = text.replace(old, new)
    (history / path.name).write_bytes(before)
    (history / (path.name + '.diff')).write_text(''.join(difflib.unified_diff(
        text.splitlines(True), after.splitlines(True), fromfile=path.name + '.before', tofile=path.name + '.after')))
    path.write_text(after)
    wiring.append({'path': str(path.relative_to(work)),
                   'before_sha256': hashlib.sha256(before).hexdigest(),
                   'after_sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
wire_record = {'status': 'WIRED_NOT_BUILT', 'actual_utc': datetime.now(timezone.utc).isoformat(),
               'edits': wiring, 'prior_versions': str(history), 'root_authorized': True}
(own / 'outputs/B80_CP29_wiring.json').write_text(json.dumps(wire_record, indent=2) + '\n')
print(json.dumps({'promotion': record, 'wiring': wire_record}, indent=2))
