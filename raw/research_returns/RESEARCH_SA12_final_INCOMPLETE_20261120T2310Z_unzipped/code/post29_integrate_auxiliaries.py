"""Integrate three fully audited auxiliary packets only after CP29 verification."""
from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess

root = Path(__file__).resolve().parents[1]
assert datetime.now(timezone.utc) >= datetime(2026, 11, 20, 21, 55, tzinfo=timezone.utc)
archive = json.loads((root / 'code/output/checkpoint29_archive_verification.json').read_text())
assert archive['full_crc'] == archive['all_manifest_hashes'] == 'PASS'
subprocess.run([
    'python3', 'code/run_logged.py', 'integrate_post29_auxiliary_packets',
    'python3', 'code/integrate_post19.py', 'post29_auxiliary',
    'parts/C/post28_research/integration_manifest_C_rank_period_generating_root_anchor.json',
    'parts/B/post28_research/integration_manifest_exceptional_Picard_unit_openness_B.json',
    'parts/D/post28_research/integration_manifest_fixed_elliptic_cone_unitary_periods_D.json'
], cwd=root, check=True)

p = root / 'parts/D/unresolved_D.tex'
s = p.read_text()
needle = 'Corollary~\\ref{D:bounded-period-arbitrary-quotient-projective-crowns}\n'
assert s.count(needle) == 1
addition = r'''Two further qualitative improvements do not complete the unbounded-period
atlas. Proposition~\ref{D:rank-period-generating-root-anchor} uses the
prime-to-characteristic local period-index theorem and one blowup of
each mixed node to obtain a generating twisted anchor of rank exactly
the geometric period $M$. Its coarse order has ordinary rank $M^2$;
rank-$r$ twisted bundles correspond to locally free order-modules of
rank $r/M$. This exact rank cancellation does not prove uniform
whole-cycle generation, syzygy or cohomology bounds for those modules.

Lemma~\ref{D:exceptional-infinitesimal-Picard-kernel} proves that a
specified Artinian punctured line comparison retains exactly its
closed-fibre exceptional divisor. Proposition
\ref{D:effective-formal-unit-family-class-openness} therefore removes
fixed determinant charts from qualitative unit-class openness for
already effective finite-type ordinary or fixed-order Morita families.
Its Serre twist is used only in comparison. It does not construct the
object family or give the required $O_R(ftr^2)$ coordinate budget.
These statements are auxiliary improvements, without another
hereditary count or an independent main-gate reduction.

'''
s = s.replace(needle, addition + needle)
old = '''No realization on one fixed geometric fundamental group is claimed.
This is an obstruction to that algebraic shortcut, not a counterexample
to the open hereditary count or a further main-gate reduction.
'''
new = r'''The subsequent construction in
\ref{D:elliptic-cone-Heisenberg-covers} and
\ref{D:fixed-elliptic-cone-unitary-geometric-periods} realizes exact
unbounded geometric periods on the puncture of one fixed elliptic
cone. A valuation restriction identifies the actual descended cyclic
algebra and proves its exact period by the unramified norm criterion.
The resulting images are nilpotent Heisenberg groups. They are not
epimorphisms onto the ambient simple unitary groups and do not refute
the open hereditary count. This is a geometric obstruction to a
uniform-period shortcut, not a further main-gate reduction.
'''
assert s.count(old) == 1
p.write_text(s.replace(old, new))

p = root / 'code/assemble.py'
s = p.read_text()
needle = "'Exact theorem locators and URLs are in the bibliography"
lines = s.splitlines(keepends=True)
summary = ('Post-checkpoint29 auxiliary integration: a rank-equal-to-period generating root anchor, '
           'exceptional infinitesimal Picard rigidity and class openness for already effective unit families, '
           'and actual unbounded unitary geometric periods on one fixed elliptic cone. '
           'All five new labelled units have four complete actual-file/source audits. '
           'The cone images are nilpotent, and the anchor/open-class results do not construct the missing '
           'uniform quantitative object atlas. No requested outcome or strongest-main-gate reduction is counted.')
for i, line in enumerate(lines):
    if line.startswith(needle):
        lines.insert(i + 1, repr(summary) + ',\n')
        break
else:
    raise AssertionError('Report insertion anchor missing.')
p.write_text(''.join(lines))
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Post-checkpoint29 auxiliary integration\n\nINCOMPLETE. '
            + datetime.now(timezone.utc).isoformat() + '. ' + summary + '\n')
print(json.dumps({'integrated_auxiliary_units': 5, 'independent_main_movement': False,
                  'requested_status_changes': [], 'checkpoint29_unchanged': True}))
