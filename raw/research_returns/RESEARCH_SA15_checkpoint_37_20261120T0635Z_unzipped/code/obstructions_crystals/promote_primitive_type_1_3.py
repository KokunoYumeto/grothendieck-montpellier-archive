"""Authorized type-(1,3) promotion after two complete independent audits."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import difflib
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
src = own / 'post_CP35_primitive_type_1_3_candidate.tex'
dst = own / 'A4_primitive_type_1_3_full_group.tex'
expected = '6c928494de0ea71b09838a8fb140823a21fdcf6e0526911047d10f023b48376d'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src) == expected and not dst.exists()
audits = [
    'outputs/root_primitive_type_1_3_audit.json',
    'agents/monodromy/outputs/independent_primitive_type_1_3_full_audit.json',
]
for name in audits:
    audit = json.loads((root / name).read_text())
    assert 'PASS' in audit['status']
    assert audit['candidate_sha256'] == expected

before = src.read_text()
labels = re.findall(r'\\label\{([^}]+)\}', before)
assert len(labels) == 7
after, n = re.subn(r'\\status\{Candidate[^}]*\}',
                    r'\\status{Proved; full independent proof, source and code audits passed.}', before)
assert n == 7 and '\\status{Candidate' not in after
assert re.sub(r'\\status\{[^}]*\}', '', before) == re.sub(r'\\status\{[^}]*\}', '', after)

con = root / 'code/consolidate.py'
cfg = root / 'notes/checkpoint36_promoted_inputs.json'
changes = root / 'notes/checkpoint36_changes.md'
con_before, cfg_before, changes_before = (p.read_text() for p in (con, cfg, changes))
anchor = (
    "   compatible_residual=a/'obstructions_crystals/A4_compatible_residual_modules.tex'\n"
    "   if compatible_residual.exists() and '\\\\status{Candidate' not in compatible_residual.read_text():\n"
    "    out.write('\\n'+compatible_residual.read_text()+'\\n')\n"
)
assert con_before.count(anchor) == 1 and dst.name not in con_before
addition = (
    "   primitive_type_one_three=a/'obstructions_crystals/A4_primitive_type_1_3_full_group.tex'\n"
    "   if primitive_type_one_three.exists() and '\\\\status{Candidate' not in primitive_type_one_three.read_text():\n"
    "    out.write('\\n'+primitive_type_one_three.read_text()+'\\n')\n"
)
con_after = con_before.replace(anchor, anchor + addition)
ast.parse(con_after)
inputs = json.loads(cfg_before)
path = str(dst.relative_to(root))
assert isinstance(inputs, list) and path not in inputs
inputs.append(path)
cfg_after = json.dumps(inputs, indent=2) + '\n'
now = datetime.now(timezone.utc).isoformat()
scope = ('Every fixed nonordinary abelian surface with an ample globally generated '
         'line bundle of type (1,3) has a nonempty smooth/sharp family and full '
         'geometric relative GL2(F2)=S3 image. Global generation is an explicit '
         'hypothesis; no general type-(1,ell), degree17, or general A.4 closure follows.')
changes_after = changes_before + (
    '\n## Audited primitive type-(1,3) source theorem\n\n'
    + 'Promoted at ' + now + ' after the complete monodromy audit at '
    '05:03:33.129281 UTC and root audit at 05:07:53.887641 UTC. '
    'The exact candidate remains unchanged; the canonical differs only in its seven status lines. '
    + scope + ' The proof supplies Frobenius-pushforward stability, the effective-divisor '
    'bound, nonzero Cartier tensor, principal-descent nodal smoothing, the actual '
    'rank-two Euler family, and Kummer/Artin–Schreier slices of orders three and two. '
    'The standalone 38-identity certificate and both unchanged isolated reruns are retained. '
    'The canonical is included once after the compatible-residual module theorem and is a '
    'required CP36 input. No build or future review was executed by this promotion.\n'
)

history = own / 'notes/CP36_primitive_type_1_3_promotion'
history.mkdir(exist_ok=False)
(history / 'candidate.tex').write_bytes(src.read_bytes())
for name, p in [('consolidate.before.py', con), ('inputs.before.json', cfg),
                ('checkpoint36_changes.before.md', changes)]:
    (history / name).write_bytes(p.read_bytes())
for name, old, new in [('promotion.diff', before, after),
                       ('consolidate.diff', con_before, con_after),
                       ('inputs.diff', cfg_before, cfg_after),
                       ('changes.diff', changes_before, changes_after)]:
    (history / name).write_text(''.join(difflib.unified_diff(
        old.splitlines(True), new.splitlines(True), fromfile='before', tofile='after')))
with dst.open('x') as f:
    f.write(after)
con.write_text(con_after)
cfg.write_text(cfg_after)
changes.write_text(changes_after)
assert sha(src) == expected and con.read_text().count(dst.name) == 1
record = {
    'status': 'PROMOTED AFTER TWO COMPLETE INDEPENDENT PROOF-SOURCE-CODE AUDITS',
    'actual_utc': now,
    'candidate': str(src.relative_to(root)), 'candidate_sha256': expected,
    'canonical': path, 'canonical_sha256': sha(dst),
    'labels': labels, 'audits': audits, 'scope': scope,
    'history': str(history.relative_to(root)),
    'candidate_changes': 'Seven status lines only; exact mathematical text and all candidate bytes preserved.',
    'shared_wiring': {
        'consolidate_sha256': sha(con), 'config_sha256': sha(cfg),
        'changes_sha256': sha(changes), 'canonical_count_in_consolidate': 1,
    },
    'numerical_scope': 'Prior author 38-identity certificate and both literal isolated reruns; no rerun claimed by this promotion.',
    'no_build_or_review_executed': True,
}
rp = own / 'primitive_type_1_3_promotion.json'
with rp.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'promotion_after_full_independent_audits',
                           path, scope, 'PROVED', str(rp.relative_to(root))]) + '\n')
with (own / 'D_results.md').open('a') as f:
    f.write('\n\n## Primitive type-(1,3) full image — ' + now + '\n\n')
    f.write(scope + '\n\nCanonical: `' + dst.name + '`. The seven-label exact candidate '
            'and complete source/code audit records are retained. The canonical changes only '
            'the statuses and is now included in CP36.\n')
print(json.dumps({'status': record['status'], 'actual_utc': now,
                  'canonical': path, 'canonical_sha256': record['canonical_sha256'],
                  'record': str(rp.relative_to(root)), 'shared_files_released': True}))
