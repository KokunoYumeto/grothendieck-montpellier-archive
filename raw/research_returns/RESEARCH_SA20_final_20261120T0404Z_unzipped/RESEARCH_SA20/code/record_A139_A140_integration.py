#!/usr/bin/env python3
"""Integrate the fully audited sphere and four-manifold obstruction proofs."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
receipt = root/'logs/A139_A140_root_integration.json'
if receipt.exists():
    raise SystemExit('A139/A140 integration already recorded')
proofs = {
    'A.139':'agents/singularities_duality/part_TOP_sphere_stabilization.tex',
    'A.140':'agents/singularities_duality/part_four_obstruction_realization.tex',
}
audits = [
    'notes/root_A139_sphere_stabilization_audit.md',
    'notes/root_A140_obstruction_realization_audit.md',
    'agents/higher_comparison/A139_independent_audit.md',
    'agents/higher_comparison/A140_independent_audit.md',
]
for statement, name in proofs.items():
    assert (root/name).read_text().count('\\begin{saresult}{'+statement+'}') == 1
for name in audits:
    assert (root/name).exists()
s140 = (root/proofs['A.140']).read_text()
assert 'L^q_6' in s140 and 'code/check\\_A140\\_product\\_spheres.py' in s140
check = json.loads((root/'logs/check_A140_product_spheres.json').read_text())
assert check['status'] == 'PASS' and check['checks'] == 1465 and check['failures'] == 0

p = root/'parts/part_A.tex'
s = p.read_text()
anchor = r'\input{agents/higher_comparison/part_finite_format_metric}'
addition = '\n'.join(r'\input{'+str(Path(v).with_suffix(''))+'}' for v in proofs.values())
assert s.count(anchor) == 1 and addition not in s
p.write_text(s.replace(anchor,anchor+'\n'+addition))

p = root/'parts/unchecked_A.tex'
s = p.read_text()
old = ('and the image of this obstruction homomorphism remain\n'
       'unevaluated in general; no target surjectivity is asserted.\n')
new = ('and the image of this obstruction homomorphism remain\n'
       'unevaluated in general. A.140 realizes the Poincar\\\'e dual of\n'
       'the Bockstein kernel when the specified quadratic assembly summand\n'
       '$I_2$ vanishes. If also $H_1(B;\\mathbb Z_{(2)})$ has no\n'
       '$2$-torsion, the obstruction homomorphism is onto. For simply\n'
       'connected $B$, the TOP component group is trivial and\n'
       '$J_B=H^2(B;\\mathbb Z/2)$; indeed ordinary TOP automorphism\n'
       'loops realize every such class. The PL automorphism comparison\n'
       'therefore fails to be onto on $\\pi_1$ when this cohomology is\n'
       'nonzero, in particular for the explicitly certified finite base\n'
       '$S^2\\times S^2$. This is not an additional higher concordance\n'
       'comparison theorem. A.139 gives the entire ordinary TOP sphere\n'
       'model as the fibre of the actual finite-rank stabilization\n'
       '$Y_n\\to Y_{n+1}$, with $Y_n=\\operatorname{hofib}(B\\mathrm O(n)\n'
       '\\to B\\mathrm{TOP}(n))$. Its four-sphere consequence gives\n'
       'vanishing only through degree three; the general base gate remains.\n')
assert old in s
p.write_text(s.replace(old,new))

p = root/'code/update_report.py'
lines = p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        line = line.replace('A.119–A.138|','A.119–A.140|')
        old = ('The endpoint predicate, J_B and the obstruction image '
               'are still unevaluated in general; no surjectivity onto the cohomology quotient is asserted.')
        new = ('The endpoint predicate, J_B and the obstruction image remain unevaluated in general. '
               'A.140 realizes the Poincare dual of the Bockstein kernel when the specified quadratic '
               'assembly summand I2 vanishes; if H1(B;Z_(2)) also has no2-torsion, lambda_B is onto '
               'and its quotient is exactly H2(B;Z/2)/J_B. For simply connected B, pi0P_TOP is trivial '
               'and J_B is all H2; ordinary TOP automorphism loops realize every class. This refutes '
               'pi1-surjectivity of the base-automorphism PL comparison for S2xS2, with an explicit '
               '1465-check finite-base certificate, but supplies no additional concordance pi1 claim. '
               'A.139 gives the entire sphere TOP model as the fibre of actual finite-rank '
               'stabilization Y_n→Y_(n+1), and safe S4 vanishing only through degree3.')
        assert old in line
        lines[i] = line.replace(old,new)
p.write_text('\n'.join(lines)+'\n')

now = datetime.now(timezone.utc).isoformat()
record = {
    'statements':['A.139','A.140'],'recorded_utc':now,
    'proofs':proofs,'audits':audits,
    'finite_checker':'code/check_A140_product_spheres.py',
    'finite_output':'logs/check_A140_product_spheres.json',
    'finite_checks':check['checks'],'finite_failures':check['failures'],
    'finite_elapsed_seconds':check['elapsed_seconds'],
    'notation':'I2 is the actual quadratic assembly summand of OPR Definition5.8; the printed theorem discrepancy is explicit',
    'original_task_status_changes':[],
    'early_progress_review_conducted':False,
}
receipt.write_text(json.dumps(record,indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A.139\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: full numbered proof, common zero-section germs, global and spherical kernels, disk fibre, exact orthogonal quotient, translated-cone and chart identification of actual stabilization, only degree0..3 S4 consequence.\n')
    f.write('A.140\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: exact OPR hypotheses and quadratic-map notation, class-level suspension identity, block/literal/ordinary distinctions, endpoint normalization, quotient and simply connected ordinary-loop realization; no extra concordance claim.\n')
    f.write('A.140\t'+now+'\tGPT-6 Astra, inherited configuration, root\tcomputation or formal certificate\tPASS: 1465 exact finite product-sphere checks, zero failures, '+str(check['elapsed_seconds'])+' seconds; mathematical product argument proves PL type and simple connectivity, program does not test TOP loop classes.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A.139 and A.140 integrated — '+now+'\n\n'
        'A.139 identifies the entire ordinary TOP sphere concordance space with the fibre of actual finite-rank stabilization, including components and the precise global/germ conventions. Its four-sphere vanishing conclusion stops at degree three. A.140 identifies the OPR obstruction with the relative cylinder class, realizes the Poincare dual of the Bockstein kernel under the exact quadratic assembly hypothesis, and obtains the full obstruction quotient when H1 has no two-torsion. For simply connected four-manifolds it evaluates J_B as all H2, and proves surjectivity of the ordinary TOP-loop obstruction. This gives an automorphism pi1 comparison counterexample on a fully specified finite S2xS2 base, certified by1465 exact checks.\n\n'
        'Root and independent full audits passed. The assembly notation discrepancy in the source is recorded explicitly. No original task row is closed, no sphere special case is substituted for the general main question, and this integration is not an early progress review.\n')
print(json.dumps(record,indent=2))
