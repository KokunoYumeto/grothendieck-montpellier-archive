from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, difflib

own = Path(__file__).resolve().parents[1]
work = own.parents[1]
stem = 'B_p5_cyclotomic_break_three_example'
expected = 'a7e4181ce539b437c10c124ff016c5a6a65d1c4747fda01f8958f93dd3cdfbd8'
sha = lambda data: hashlib.sha256(data).hexdigest()
candidate = own / (stem + '_candidate.tex')
raw = candidate.read_bytes()
assert sha(raw) == expected
root = json.loads((work / 'outputs/root_B89_audit.json').read_text())
oc = json.loads((own.parent / 'obstructions_crystals/B89_independent_audit.json').read_text())
assert all('PASS' in a['status'] and a['candidate_sha256'] == expected for a in (root, oc))
pre = own / ('notes/' + stem + '.prepromotion.tex')
assert not pre.exists()
pre.write_bytes(raw)
s = re.sub(r'\\status\{Candidate[^}]*\}',
           lambda _: r'\status{Proved; full independent root and companion audits passed.}',
           raw.decode())
s = s.replace(s.splitlines()[0], '% Proved base-field example after complete audits; no BT comparison is constructed.', 1)
paragraph = ('\n\\smallskip\n\\noindent\\emph{Independent audits.}\n'
             'The complete root and companion proof and code audits passed.\n'
             'Their literal author-output-preserving reruns took\n'
             f"\\({root['independent_runtime_seconds']}\\) and\n"
             f"\\({oc['independent_runtime_seconds']}\\) seconds, respectively.\n"
             'Both audits reread the complete B60 and B88 dependencies;\n'
             'neither claims a new external-source opening. The exact\n'
             'candidate, failed and successful programs, outputs, and\n'
             'promotion diff remain retained.\n')
assert s.count(r'\end{remark}') == 1
s = s.replace(r'\end{remark}', paragraph + r'\end{remark}')
canonical = own / (stem + '.tex')
assert not canonical.exists()
canonical.write_text(s)
labels = re.findall(r'\\label\{([^}]+)\}', s)
assert labels == root['labels'] == oc['labels'] and len(labels) == 2
now = datetime.now(timezone.utc).isoformat()
scope = ('Explicit allowed p5/e20 base with cyclotomic degree-five break3, '
         'degree-25 cyclotomic125 image, and break72 after tame24 extension. '
         'Base/cyclotomic realization only; no height-two BT group, common torsion '
         'comparison, ambiguous pair, least-index lower example, or main-gate closure.')
record = {
    'status': 'PROVED', 'promotion_utc': now, 'canonical': str(canonical),
    'canonical_sha256': sha(canonical.read_bytes()),
    'audited_candidate_sha256': expected, 'preserved_candidate': str(pre),
    'labels': labels, 'scope': scope,
    'root_audit': '../../outputs/root_B89_audit.json',
    'root_audit_utc': root['actual_utc'],
    'root_runtime_seconds': root['independent_runtime_seconds'],
    'companion_audit': '../obstructions_crystals/B89_independent_audit.json',
    'companion_audit_utc': oc['actual_utc'],
    'companion_runtime_seconds': oc['independent_runtime_seconds'],
    'author_runtime_seconds': root['author_runtime_seconds'],
    'source_scope': 'Full internal B60 and B88 proofs reread; no new external-source access claimed.',
    'checkpoint_scope': 'Post-CP31 canonical for CP32; immutable CP31 unchanged.',
    'retained_failure': root['author_retained_failure'],
}
(own / 'outputs/B89_promotion.json').write_text(json.dumps(record, indent=2) + '\n')
(own / 'notes/B89_promotion.diff').write_text(''.join(difflib.unified_diff(
    raw.decode().splitlines(True), s.splitlines(True),
    fromfile=candidate.name, tofile=canonical.name)))
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join((now, label, 'PROVED_FULL_AUDITS', scope,
                           stem + '.tex;outputs/B89_promotion.json',
                           'Full root+OC proof/code audits; no main-gate movement')) + '\n')
with (own / 'STATUS_CURRENT.md').open('a') as f:
    f.write(f'\n## {now} — B89 promoted\n\n{scope}\n')
path = work / 'code/consolidate.py'
before = path.read_bytes()
text = before.decode()
old = "'B_p5_full_image_ramification.tex']:"
new = "'B_p5_full_image_ramification.tex',\n                    'B_p5_cyclotomic_break_three_example.tex']:"
assert text.count(old) == 1
after = text.replace(old, new)
history = own / 'notes/CP32_before_B89_wiring'
history.mkdir(exist_ok=False)
(history / path.name).write_bytes(before)
(history / (path.name + '.diff')).write_text(''.join(difflib.unified_diff(
    text.splitlines(True), after.splitlines(True),
    fromfile='consolidate.before', tofile='consolidate.after')))
path.write_text(after)
wiring = {'status': 'CONSOLIDATE_WIRED_NOT_BUILT',
          'actual_utc': datetime.now(timezone.utc).isoformat(),
          'path': 'code/consolidate.py', 'before_sha256': sha(before),
          'after_sha256': sha(path.read_bytes()), 'prior_versions': str(history),
          'change': 'One B89 insertion immediately after B88; no other content changed.',
          'workflow_scope': 'Parent owns CP32 prepare/update; no workflow or bibliography edited.'}
(own / 'outputs/B89_CP32_wiring.json').write_text(json.dumps(wiring, indent=2) + '\n')
print(json.dumps({'promotion': record, 'wiring': wiring}, indent=2))
