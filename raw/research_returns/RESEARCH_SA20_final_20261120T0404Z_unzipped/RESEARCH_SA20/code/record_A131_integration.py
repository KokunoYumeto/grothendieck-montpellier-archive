#!/usr/bin/env python3
"""Record the audited effective full-space reduction without closing A.1(b)."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
assert r'\begin{saresult}{A.131}' in (root / 'parts/parametric_concordance.tex').read_text()
receipt = root / 'logs/A131_root_integration.json'
if receipt.exists():
    raise SystemExit('A131 root integration already recorded')
check = json.loads((root / 'logs/root_A131_pl_codes.json').read_text())
assert check['status'] == 'PASS' and check['test_count'] == 30
assert all(t['pass'] for t in check['tests'])
p = root / 'code/update_report.py'
lines = p.read_text().splitlines()
replacement = ('A.1(b)|Unsettled; strictly reduced to comparison gates|'
    'A.103,A.113–A.116,A.119–A.131|'
    'A.131 gives complete effective countable simplicial-group models for the entire PL and semialgebraic concordance spaces in every dimension over every real closed field. Valid finite integer codes and equality are decidable, all structure operations are total algorithms, and the full Moore quotient gives recursive presentations of every homotopy group. A.113 identifies the PL component presentation with the definable component group in every fixed o-minimal expansion. The real TOP space has the same complete model when every base component has dimension at least five. These are exhaustive countable presentations, not finite classical invariant decompositions or terminating isotopy decisions. The earlier E(K), low-dimensional vanishings, stable models and A.130 subgroup theorem remain more structural results in their stated scopes. The remaining original gates are higher PL-to-SA/arbitrary-definable comparison and the low-dimensional real PL-to-TOP comparison. In dimensions at least five PL-to-SA is injective in every degree and an isomorphism on components and pi1; real pi2 surjectivity, already for T6, is the first remaining higher comparison. The computable map between the two algebraic models does not establish a weak equivalence. No higher effective reduction for an arbitrary o-minimal expansion is asserted.')
found = 0
for i, line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        lines[i] = replacement
        found += 1
assert found == 1
p.write_text('\n'.join(lines) + '\n')
now = datetime.now(timezone.utc).isoformat()
record = {
    'statement': 'A.131', 'recorded_utc': now,
    'root_proof_audit': 'notes/root_A131_effective_model_audit.md',
    'independent_audit': 'agents/tensor_and_finite/notes/A131/independent_audit.md',
    'root_certificate': 'logs/root_A131_pl_codes.json',
    'checks': check['test_count'], 'elapsed_seconds': check['elapsed_seconds'],
    'main_gate_strictly_reduced': True,
    'original_A1b_complete': False,
    'resolved_scope': 'Whole effective PL and SA simplicial models; all recursive homotopy presentations; definable components all dimensions; real TOP whole model in base dimension at least five.',
    'retained_gates': [
        'Higher PL-to-SA comparison; first remaining degree pi2 in the established dimension-at-least-five comparison range.',
        'Higher families for an arbitrary fixed o-minimal expansion.',
        'Low-dimensional real PL-to-TOP concordance comparison.'
    ],
    'not_claimed': ['finite invariant-factor evaluation', 'terminating isotopy decision', 'manifold recognition', 'arbitrary-real-number computation']
}
receipt.write_text(json.dumps(record, indent=2) + '\n')
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A.131 effective whole-space computation integrated — ' + now + '\n\n'
        'A.131 has passed the author, independent and root mathematical audits, exact original-source checks, and three independently recorded finite-checker executions. The root execution passed 30 exact-arithmetic tests in ' + str(check['elapsed_seconds']) + 's. The result gives decidable finite simplex codes, computable group/simplicial operations, and complete recursive Moore presentations for every homotopy group of the full PL and semialgebraic concordance spaces, including all unstable dimensions. The entire countable simplicial model also retains the higher attachment data.\n\n'
        'This strictly reduces the main A.1 gate: the separate effective unstable PL/SA full-space computation is now supplied, and the real TOP model follows in base dimension at least five. All definable component groups have the resulting PL presentation. No finite classical decomposition or terminating isotopy decision is claimed. A.1(b) remains unsettled because higher PL-to-SA/arbitrary-o-minimal comparison and the low-dimensional real PL-to-TOP comparison remain. The historical ledger is preserved; the current table replaces its older gate descriptions only prospectively.\n')
with (root / 'notes/root_checks.tsv').open('a') as f:
    f.write('A.131\t' + now + '\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: complete effective simplex-code and Moore-presentation proof; A115/A116 parameter-preserving dependencies rechecked; opened BPR exact algorithms and visually inspected May pp64–69. Original A1b remains open on comparison gates.\n')
    f.write('A.131\t' + now + '\tGPT-6 Astra, inherited configuration, root\tcomputation or formal certificate\tPASS: 30 exact Fraction tests, B=point and parameter dimensions0–2, elapsed ' + str(check['elapsed_seconds']) + 's; full checker source read; no general QE implementation or nonzero homotopy detection claimed.\n')
print(json.dumps(record, indent=2))
