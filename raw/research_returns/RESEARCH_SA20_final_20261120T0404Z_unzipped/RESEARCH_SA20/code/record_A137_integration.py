#!/usr/bin/env python3
"""Integrate the fully audited base-four component-image criterion once."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
receipt = root/'logs/A137_root_integration.json'
if receipt.exists():
    raise SystemExit('A137 integration already recorded')
proof = root/'agents/singularities_duality/part_base_four_component_image.tex'
assert proof.exists() and proof.read_text().count(r'\begin{saresult}{A.137}') == 1
audits = ['notes/root_A137_component_image_audit.md',
          'agents/higher_comparison/A137_independent_audit.md']
for name in audits:
    assert (root/name).exists(), name

p = root/'parts/part_A.tex'
s = p.read_text()
anchor = r'\input{agents/singularities_duality/part_base_four_stabilization}'
addition = r'\input{agents/singularities_duality/part_base_four_component_image}'
assert s.count(anchor) == 1 and addition not in s
p.write_text(s.replace(anchor, anchor+'\n'+addition))

p = root/'parts/unchecked_A.tex'
s = p.read_text()
old = ('$F_A$ and this actual map remains, as does the separate cokernel\n'
       'of $\\pi_0P_{\\mathrm{PL}}\\to\\pi_0P_{\\mathrm{TOP}}$.\n'
       'No TOP concordance component without a PL representative is\n'
       'determined by the based-fibre calculation.\n')
new = ('$F_A$ and this actual map remains. A.137 gives the separate\n'
       'complete component-image criterion: first the TOP endpoint must\n'
       'be isotopic to a PL map; after choosing such an isotopy, its\n'
       'relative cylinder class must vanish modulo\n'
       '$J_B=\\operatorname{im}(\\pi_0\\beta_B)$. On the subgroup\n'
       '$I_B$ satisfying the endpoint condition this is a homomorphism\n'
       'to $H^2(B;\\mathbb Z/2)/J_B$ with kernel precisely the PL\n'
       'concordance image. Thus $I_B$ modulo that image is a finite\n'
       'elementary abelian $2$-group. The endpoint predicate, $J_B$,\n'
       'and the image of this obstruction homomorphism remain\n'
       'unevaluated in general; no target surjectivity is asserted.\n')
assert old in s
p.write_text(s.replace(old, new))

p = root/'code/update_report.py'
lines = p.read_text().splitlines()
for i, line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        line = line.replace('A.119–A.136|', 'A.119–A.137|')
        old = ('Evaluation of the base-automorphism comparison and this actual map remains, '
               'together with the separate cokernel of pi0PL→pi0TOP; TOP components with no PL representative are not determined.')
        new = ('Evaluation of the base-automorphism comparison and this actual map remains. '
               'A.137 gives the complete component-image criterion: the TOP endpoint must be isotopic to PL, '
               'and its normalized relative cylinder class must vanish modulo J_B=im(pi0beta_B). '
               'On the endpoint-image subgroup I_B, this defines a homomorphism to H2(B;Z/2)/J_B '
               'with kernel exactly the PL concordance image. The corresponding quotient is therefore '
               'a finite elementary abelian2 group. The endpoint predicate, J_B and the obstruction image '
               'are still unevaluated in general; no surjectivity onto the cohomology quotient is asserted.')
        assert old in line
        lines[i] = line.replace(old, new)
p.write_text('\n'.join(lines)+'\n')

now = datetime.now(timezone.utc).isoformat()
record = {
    'statement':'A.137', 'recorded_utc':now,
    'where_proved':str(proof.relative_to(root)), 'audits':audits,
    'scope':'Closed compact real PL four-manifolds; ordinary free-top concordance components',
    'proved':'lambda_B:I_B→H2(B;Z/2)/im(pi0beta_B) is a homomorphism with kernel precisely the PL component image; quotient finite elementary abelian2',
    'remaining':'Evaluate ordinary endpoint-image predicate, stabilization image J_B, obstruction image and full higher comparison; no original row closed',
    'original_A1b_complete':False, 'early_progress_review_conducted':False,
    'finite_counterexample_claimed':False
}
receipt.write_text(json.dumps(record, indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A.137\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: full relative orbit zero-test, affine KS rule and trivial action, explicit endpoint traces, all lift and representative choices, ordinary-component invariance, exact kernel and finite quotient; unevaluated endpoint and stabilization image retained.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A.137 integrated — '+now+'\n\n'
        'For a closed compact real PL four-manifold, the image on ordinary free-top concordance components now has a complete criterion. Its endpoint must be TOP-isotopic to PL. After choosing such an isotopy, the relative cylinder KS class must be zero modulo J_B=im(pi_0 beta_B). This is a homomorphism on the endpoint-image subgroup I_B, with kernel exactly the PL concordance image; the resulting quotient embeds in H^2(B;Z/2)/J_B and is finite elementary abelian2. The proof controls every choice and uses genuine ordinary isotopies. Root and independent full audits passed.\n\n'
        'The endpoint-image predicate, J_B and the actual obstruction image remain unevaluated in general. No surjectivity or original-task completion is claimed. The scheduled review will compare this criterion with the previous component-cokernel gate; this integration note is not an early review and does not reset the stopping count.\n')
print(json.dumps(record, indent=2))
