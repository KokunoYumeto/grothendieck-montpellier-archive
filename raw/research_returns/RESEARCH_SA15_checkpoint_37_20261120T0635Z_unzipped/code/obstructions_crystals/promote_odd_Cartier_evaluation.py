"""Authorized status-only odd-polarization promotion and narrow CP36 wiring."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import difflib
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
src = own / 'post_CP35_odd_Cartier_evaluation_candidate.tex'
dst = own / 'A4_odd_Cartier_evaluation.tex'
expected = '85858ad8cd397209af2b7e1d3b833c4ecee0ac5fa529928c46de99ddedba7acb'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src) == expected and not dst.exists()
audits = ['outputs/root_odd_Cartier_evaluation_audit.json',
          'agents/monodromy/outputs/independent_odd_Cartier_evaluation_audit.json']
for path in audits:
    record = json.loads((root / path).read_text())
    assert 'PASS' in record['status'] and record['candidate_sha256'] == expected
before = src.read_text()
labels = re.findall(r'\\label\{([^}]+)\}', before)
after, count = re.subn(r'\\status\{Candidate[^}]*\}',
                       r'\\status{Proved; full independent proof and source audits passed.}', before)
assert count == len(labels) == 5
assert re.sub(r'\\status\{[^}]*\}', '', before) == re.sub(r'\\status\{[^}]*\}', '', after)
con = root / 'code/consolidate.py'
cfg = root / 'notes/checkpoint36_promoted_inputs.json'
changes = root / 'notes/checkpoint36_changes.md'
log = root / 'notes/ROOT_SEARCH_LOG_36.md'
paths = [con, cfg, changes, log]
old = {p: p.read_text() for p in paths}
anchor = (
    "   primitive_type_one_three=a/'obstructions_crystals/A4_primitive_type_1_3_full_group.tex'\n"
    "   if primitive_type_one_three.exists() and '\\\\status{Candidate' not in primitive_type_one_three.read_text():\n"
    "    out.write('\\n'+primitive_type_one_three.read_text()+'\\n')\n"
)
addition = (
    "   odd_Cartier_evaluation=a/'obstructions_crystals/A4_odd_Cartier_evaluation.tex'\n"
    "   if odd_Cartier_evaluation.exists() and '\\\\status{Candidate' not in odd_Cartier_evaluation.read_text():\n"
    "    out.write('\\n'+odd_Cartier_evaluation.read_text()+'\\n')\n"
)
assert old[con].count(anchor) == 1 and dst.name not in old[con]
new = {con: old[con].replace(anchor, anchor + addition)}
ast.parse(new[con])
relative = str(dst.relative_to(root))
inputs = json.loads(old[cfg])
assert isinstance(inputs, list) and relative not in inputs
inputs.append(relative)
new[cfg] = json.dumps(inputs, indent=2) + '\n'
now = datetime.now(timezone.utc).isoformat()
scope = ('For every ample globally generated L of odd N=chi(L)>1 on an abelian '
         'surface in characteristic two, the Frobenius-pushforward evaluation has '
         'generic rank at least three, and has rank four when gcd(N,6)=1. '
         'On a nonordinary surface the actual global Cartier tensor is surjective. '
         'No everywhere-generation, individual global-contraction rank, smooth-member '
         'or full-monodromy conclusion follows from this theorem alone.')
new[changes] = old[changes] + (
    '\n## Audited odd-polarization Cartier and evaluation theorem\n\n'
    'Promoted at ' + now + ' after full companion and root proof/source audits '
    'at05:25:54.688299 and05:32:30.953115 UTC. ' + scope + ' The exact candidate '
    'is unchanged; only five status lines differ in the canonical. The canonical '
    'follows the primitive type-(1,3) stability dependency and is required by CP36. '
    'No numerical check is needed or claimed, and no build or future review was executed.\n'
)
new[log] = old[log] + (
    '\n## Odd-polarization Cartier and generic evaluation\n\n'
    'The complete five-label theorem was promoted at ' + now + ' after root and '
    'monodromy full audits. The retained original Edixhoven–van der Geer–Moonen '
    'AV proofs7.22–7.26,8.19–8.20 and8.24–8.28 were actually read in the author '
    'and auditor scopes recorded in their JSON files. The just-audited odd-chi '
    'Frobenius stability proof is the internal dependency. Hodge index and the '
    'standard numerical-triviality/torsion theorem for divisors are used explicitly; '
    'AV7.23/7.25 remove NS torsion. Search snippets were only provenance cross-checks, '
    'and no new original proof of that general numerical-divisor theorem is claimed. '
    'There is no numerical experiment. Exact source scopes and limitations are in '
    'agents/obstructions_crystals/odd_Cartier_evaluation_candidate_record.json and '
    'outputs/root_odd_Cartier_evaluation_audit.json.\n'
)
history = own / 'notes/CP36_odd_Cartier_evaluation_promotion'
history.mkdir(exist_ok=False)
(history / 'candidate.tex').write_bytes(src.read_bytes())
(history / 'promotion.diff').write_text(''.join(difflib.unified_diff(
    before.splitlines(True), after.splitlines(True), fromfile='candidate', tofile='canonical')))
for path in paths:
    (history / (path.name + '.before')).write_bytes(path.read_bytes())
    (history / (path.name + '.diff')).write_text(''.join(difflib.unified_diff(
        old[path].splitlines(True), new[path].splitlines(True), fromfile='before', tofile='after')))
with dst.open('x') as f:
    f.write(after)
for path in paths:
    path.write_text(new[path])
assert sha(src) == expected and con.read_text().count(dst.name) == 1
record = {'status': 'PROMOTED AFTER TWO FULL PROOF-SOURCE AUDITS', 'actual_utc': now,
          'candidate': str(src.relative_to(root)), 'candidate_sha256': expected,
          'canonical': relative, 'canonical_sha256': sha(dst), 'labels': labels,
          'audits': audits, 'scope': scope, 'status_only_changes': count,
          'history': str(history.relative_to(root)),
          'shared_files': {str(p.relative_to(root)): sha(p) for p in paths},
          'numerical_run': None, 'no_build_or_review_executed': True}
rp = own / 'odd_Cartier_evaluation_promotion.json'
with rp.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'promotion_after_full_independent_audits',
                           relative, scope, 'PROVED', str(rp.relative_to(root))]) + '\n')
with (own / 'D_results.md').open('a') as f:
    f.write('\n\n## Odd-polarization Cartier/evaluation — ' + now + '\n\n' + scope
            + '\n\nCanonical: `' + dst.name + '`. Full audit and status-only promotion '
              'records are retained; the CP36 input follows its primitive stability dependency.\n')
print(json.dumps({'status': record['status'], 'actual_utc': now,
                  'canonical': relative, 'canonical_sha256': record['canonical_sha256'],
                  'record': str(rp.relative_to(root)), 'shared_files_released': True}))
