#!/usr/bin/env python3
"""Integrate audited comparison results while retaining the parent task's open scopes."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
receipt = root / 'logs/A132_A133_root_integration.json'
if receipt.exists():
    raise SystemExit('A132/A133 integration already recorded')
assert r'\begin{saresult}{A.132}' in (root/'parts/parametric_concordance.tex').read_text()
assert r'\begin{saresult}{A.133}' in (root/'agents/higher_comparison/part_elementary_extensions.tex').read_text()
assert r'\input{agents/higher_comparison/part_elementary_extensions}' in (root/'parts/part_A.tex').read_text()
certificate = json.loads((root/'logs/root_A132_sphere.json').read_text())
assert certificate['outcome'] == 'PASS' and certificate['checks'] == 53
now = datetime.now(timezone.utc).isoformat()

p = root/'code/update_report.py'
lines = p.read_text().splitlines()
replacement = ('A.1(b)|Unsettled; full PL/SA models and a refuted unrestricted PL–TOP comparison|'
 'A.103,A.113–A.116,A.119–A.133|'
 'A.131 gives complete effective countable simplicial-group models for the entire PL and semialgebraic concordance spaces in every dimension over every real closed field. Valid finite integer codes and equality are decidable, all structure operations are total algorithms, and the full Moore quotient gives recursive presentations of every homotopy group. A.113 identifies the PL component presentation with the definable component group in every fixed o-minimal expansion. The real TOP space has the same complete model when every base component has dimension at least five. A.132 now refutes the unrestricted PL-to-TOP weak-equivalence claim: for the standard three-sphere the PL pi2 is zero and TOP pi2 is Z/2; its actual free-top TOP space has the proved model Omega(TOP(4)/O(4)). A.133 proves whole-space invariance under elementary extension in one fixed o-minimal language, and transfers comparison properties across models of a complete theory, with a real-model corollary only when one exists. These results do not complete the general low-dimensional real comparison or higher PL-to-SA/arbitrary-definable comparison. In dimensions at least five PL-to-SA is injective in every degree and an isomorphism on components and pi1; real pi2 surjectivity, already for T6, remains the first higher gate in that range. The algebraic models are exhaustive countable presentations, not finite classical invariant decompositions or terminating isotopy decisions. The countable-model corollary for arbitrary expansions is not a decidable or oracle-free effective computation. The earlier E(K), low-dimensional vanishings, stable models and A.130 subgroup theorem retain their stated scopes.')
found = 0
for i,line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        lines[i] = replacement
        found += 1
assert found == 1
# Newly active agents supply independently authored provenance as well.
for i,line in enumerate(lines):
    if line.startswith("for sub,title in [('tensor_and_finite'"):
        lines[i] = "for sub,title in [('tensor_and_finite','B, E and A.6'),('singularities_duality','C'),('lie_theory','D'),('higher_comparison','higher concordance comparison'),('maximal_locus','maximal-locus method audits')]:"
p.write_text('\n'.join(lines)+'\n')
record = {
 'statements':['A.132','A.133'], 'recorded_utc':now,
 'A132_root_audit':'notes/root_A132_TOP_S3_audit.md',
 'A132_independent_audit':'agents/higher_comparison/A132_independent_audit.md',
 'A133_root_audit':'notes/root_A133_elementary_extension_audit.md',
 'A132_finite_base_checks':53,
 'A132_root_runtime_seconds':certificate['runtime_seconds'],
 'original_A1b_complete':False,
 'comparison_refuted':'Unrestricted real PL-to-TOP weak equivalence; explicit pi2 discrepancy on S3.',
 'retained_gates':['Higher PL-to-SA and arbitrary fixed o-minimal comparison','Full low-dimensional real comparison beyond the proved S3 model/discrepancy'],
 'not_claimed':['Finite classical computation','Effective elementary diagram for arbitrary o-minimal structures','A PL-to-SA counterexample','A complete general low-dimensional comparison']
}
receipt.write_text(json.dumps(record,indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A.132\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: entire relative germ-lifting, strict free-top kernel, identity-component comparison, and natural homotopy-fibre model checked; original Hatcher605–606/FQ128/KS251 visually inspected and E–K/GGHKP/BL exact passages reopened.\n')
    f.write('A.132\t'+now+'\tGPT-6 Astra, inherited configuration, root\tcomputation or formal certificate\tPASS:53 exact finite-base checks in'+str(certificate['runtime_seconds'])+'s; all sphere links, integral Smith forms, homology and primitive cycle checked. This does not test the TOP family.\n')
    f.write('A.133\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: complete final numbered proof and marked-set extension; graph Hardt cells, definable compact inverse, exact boundary transfer, common elementary extension and real-model limitation checked against opened Coste locators.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A.132 and A.133 integrated — '+now+'\n\n'
    'The unrestricted real PL–TOP weak comparison is false. A.132 proves the full free-top S3 TOP model Omega(TOP(4)/O(4)) and the exact discrepancy pi2PL=0 versus pi2TOP=Z/2, with trivial components and pi1 on both sides. The complete proof passed the author, independent higher-comparison and root audits. Root separately checked the finite sphere base with53 exact tests in'+str(certificate['runtime_seconds'])+'seconds; this is not a computational test of the TOP class.\n\n'
    'A.133 proves full concordance-space invariance under elementary extension of one o-minimal language, with compact marked-set and common-complete-theory versions. Its real-model corollary preserves the explicit hypothesis that a real model exists. A countable elementary submodel is not asserted to have a decidable elementary diagram. The main A1b row remains incomplete on higher PL–SA/arbitrary-definable comparison and the full low-dimensional real comparison. The original70-row table records these distinctions; neither result silently closes the parent task.\n')
print(json.dumps(record,indent=2))
