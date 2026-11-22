"""Authorized CR promotion and paired CP35 wiring after two full audits."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import difflib
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
src = own / 'post_CP34_compatible_residual_modules_candidate.tex'
dst = own / 'A4_compatible_residual_modules.tex'
wedge = own / 'A4_Lang_wedge_pole_theta_bound.tex'
expected = 'ccdb387fc0b28ecadecdfa7dc1c8b093d706c6f5151555239551b322ad098f74'
wedge_expected = '4bc8feec42673f6863d2bd864fd7bce98d509011c6e64251cd421682f77d5a3c'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src) == expected and not dst.exists()
assert sha(wedge) == wedge_expected
audits = [
    'outputs/root_compatible_residual_modules_audit.json',
    'agents/monodromy/outputs/independent_compatible_residual_modules_audit.json',
]
for name in audits:
    audit = json.loads((root / name).read_text())
    assert 'PASS' in audit['status']
    assert audit['candidate_sha256'] == expected

before = src.read_text()
labels = re.findall(r'\\label\{([^}]+)\}', before)
assert len(labels) == 4
after = re.sub(r'\\status\{Candidate[^}]*\}',
               r'\\status{Proved; full independent proof audits passed.}', before)
after = re.sub(r'\A%[^\n]*',
               '% Promoted after final root and monodromy audits; all candidate versions retained.', after)
old_scope = ('The final corollary is conditional on completion of the separate\n'
             'determinant-wedge proof audits. Even with that bound, the source\n')
new_scope = ('The final corollary uses the separately proved determinant-wedge\n'
             'theorem. Even with that bound, the source\n')
assert after.count(old_scope) == 1
after = after.replace(old_scope, new_scope)
assert after.count('\\status{Proved') == 4

con = root / 'code/consolidate.py'
con_before = con.read_text()
anchor = (
    "   compatible_intermediates=a/'monodromy/compatible_cyclic_intermediates.tex'\n"
    "   if compatible_intermediates.exists() and '\\\\status{Candidate' not in compatible_intermediates.read_text():\n"
    "    out.write('\\n'+compatible_intermediates.read_text()+'\\n')\n"
)
assert con_before.count(anchor) == 1
assert wedge.name not in con_before and dst.name not in con_before
addition = (
    "   lang_wedge_bound=a/'obstructions_crystals/A4_Lang_wedge_pole_theta_bound.tex'\n"
    "   if lang_wedge_bound.exists() and '\\\\status{Candidate' not in lang_wedge_bound.read_text():\n"
    "    out.write('\\n'+lang_wedge_bound.read_text()+'\\n')\n"
    "   compatible_residual=a/'obstructions_crystals/A4_compatible_residual_modules.tex'\n"
    "   if compatible_residual.exists() and '\\\\status{Candidate' not in compatible_residual.read_text():\n"
    "    out.write('\\n'+compatible_residual.read_text()+'\\n')\n"
)
con_after = con_before.replace(anchor, anchor + addition)
ast.parse(con_after)
cfg = root / 'notes/checkpoint35_promoted_inputs.json'
cfg_before = cfg.read_text()
inputs = json.loads(cfg_before)
assert isinstance(inputs, list)
new_paths = [str(wedge.relative_to(root)), str(dst.relative_to(root))]
assert all(p not in inputs for p in new_paths)
inputs.extend(new_paths)
cfg_after = json.dumps(inputs, indent=2) + '\n'

history = own / 'notes/CP35_compatible_residual_promotion'
history.mkdir(exist_ok=False)
(history / 'candidate.tex').write_bytes(src.read_bytes())
(history / 'consolidate.before.py').write_bytes(con.read_bytes())
(history / 'inputs.before.json').write_bytes(cfg.read_bytes())
for name, old, new in [
    ('promotion.diff', before, after),
    ('consolidate.diff', con_before, con_after),
    ('inputs.diff', cfg_before, cfg_after),
]:
    (history / name).write_text(''.join(difflib.unified_diff(
        old.splitlines(True), new.splitlines(True), fromfile='before', tofile='after')))

with dst.open('x') as f:
    f.write(after)
con.write_text(con_after)
cfg.write_text(cfg_after)
assert sha(src) == expected and sha(wedge) == wedge_expected
assert con.read_text().count(wedge.name) == 1
assert con.read_text().count(dst.name) == 1
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'PROMOTED AFTER TWO COMPLETE INDEPENDENT PROOF AUDITS',
    'actual_utc': now,
    'candidate': str(src.relative_to(root)),
    'candidate_sha256': expected,
    'canonical': str(dst.relative_to(root)),
    'canonical_sha256': sha(dst),
    'labels': labels,
    'audits': audits,
    'history': str(history.relative_to(root)),
    'scope': ('Actual source residual projections and compatible same-fibre direct-sum inclusion. '
              'Combining the determinant-wedge bound with cyclic deck-module divisibility gives '
              'quotient dimension at least872 and residual dimension at most1728 at degree17. '
              'No residual-module vanishing or unconditional full image is asserted.'),
    'changes': ('Only short Proved statuses, provenance comment and the completed wedge-audit '
                'metadata changed in the candidate. The wedge canonical is unchanged. Both '
                'optional includes and CP35 required paths were added exactly once in dependency order.'),
    'computation': 'No numerical computation needed or claimed.',
    'shared_wiring': {
        'paths_in_order': new_paths,
        'consolidate_sha256': sha(con),
        'config_sha256': sha(cfg),
        'wedge_canonical_sha256': wedge_expected,
    },
}
rp = own / 'compatible_residual_modules_promotion.json'
with rp.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([
            now, label, 'promotion_after_full_independent_audits', record['canonical'],
            record['scope'], 'PROVED; quantitative bound only', str(rp.relative_to(root)),
        ]) + '\n')
    f.write('\t'.join([
        now, 'CP35-wedge-and-compatible-residual-wiring', 'authorized_shared_wiring',
        'code/consolidate.py', 'Both audited canonicals included once in dependency order; CP35 config updated.',
        'PASS; no build or finalizer executed', str(rp.relative_to(root)),
    ]) + '\n')
with (own / 'D_results.md').open('a') as f:
    f.write('\n\n## Compatible residual modules and the rounded prime bound — ' + now + '\n\n')
    f.write('`A4_compatible_residual_modules.tex` proves that projection of the target residual '
            'module to an odd source lands in that source\'s canonical residual module, without '
            'assuming the source image is full. Compatible cyclic intermediates place all these '
            'modules in disjoint sectors of one actual fibre. The wedge bound and the exact '
            'Frobenius-orbit dimension of nontrivial cyclic modules yield the rounded bound; '
            'at degree17 the quotient has dimension at least872 and the residual module at most1728. '
            'Both canonicals are now wired for CP35. Full image remains unproved in that degree.\n')
print(json.dumps({
    'status': record['status'], 'actual_utc': now,
    'canonical': record['canonical'], 'canonical_sha256': record['canonical_sha256'],
    'record': str(rp.relative_to(root)), 'shared_paths': new_paths,
    'shared_files_released': True,
}))
