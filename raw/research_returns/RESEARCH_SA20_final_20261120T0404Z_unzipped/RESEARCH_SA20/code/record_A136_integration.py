#!/usr/bin/env python3
"""Integrate the audited explicit four-dimensional stabilization model."""
from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parents[1]
receipt=root/'logs/A136_root_integration.json'
if receipt.exists():
    raise SystemExit('A136 integration already recorded')
proof=root/'agents/singularities_duality/part_base_four_stabilization.tex'
assert proof.exists() and proof.read_text().count(r'\begin{saresult}{A.136}')==1
audits=['notes/root_A136_stabilization_model_audit.md','agents/higher_comparison/A136_independent_audit.md']
for name in audits:
    assert (root/name).exists(),name

p=root/'parts/part_A.tex';s=p.read_text()
anchor=r'\input{agents/singularities_duality/part_base_four_comparison}'
addition=r'\input{agents/singularities_duality/part_base_four_stabilization}'
assert s.count(anchor)==1 and addition not in s
p.write_text(s.replace(anchor,anchor+'\n'+addition))

p=root/'parts/unchecked_A.tex';s=p.read_text()
old=('comparison fibre. The latter space, connecting maps and extension\n'
     'data remain; this exact sequence is not a complete computation\n'
     'of the original free-top comparison.\n')
new=('comparison fibre. A.136 strengthens this to an explicit based-fibre\n'
     'model: $F_P\\simeq\\operatorname{hofib}(\\beta_B)$, where\n'
     '$\\beta_B:F_A\\to\\operatorname{Map}(B,K(\\mathbb Z/2,2))$\n'
     'is the loop of product-with-a-line stabilization on sliced PL\n'
     'structures, followed by the open five-dimensional classification.\n'
     'Thus the extension map is specified, with a relative cylinder\n'
     'obstruction in $H^2(B;\\mathbb Z/2)$ on components. Evaluating\n'
     '$F_A$ and this actual map remains, as does the separate cokernel\n'
     'of $\\pi_0P_{\\mathrm{PL}}\\to\\pi_0P_{\\mathrm{TOP}}$.\n'
     'No TOP concordance component without a PL representative is\n'
     'determined by the based-fibre calculation.\n')
assert old in s
p.write_text(s.replace(old,new))

p=root/'code/update_report.py';lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        line=line.replace('A.119–A.135|','A.119–A.136|')
        old='The base-automorphism comparison and its connecting/extension data remain undetermined; the sequence is not a full free-top calculation.'
        new=('A.136 specifies the extension map: the entire based comparison fibre is hofib(beta_B), '
             'where beta_B:F_A→Map(B,K(Z/2,2)) is looped product-with-line stabilization on sliced PL structures. '
             'Its component obstruction is the relative cylinder class in H2(B;Z/2). '
             'Evaluation of the base-automorphism comparison and this actual map remains, together with the separate '
             'cokernel of pi0PL→pi0TOP; TOP components with no PL representative are not determined.')
        assert old in line
        lines[i]=line.replace(old,new)
p.write_text('\n'.join(lines)+'\n')

now=datetime.now(timezone.utc).isoformat()
record={'statement':'A.136','recorded_utc':now,'where_proved':str(proof.relative_to(root)),
        'audits':audits,'scope':'Closed compact real PL four-manifolds; full based comparison fibres',
        'proved':'F_P is the homotopy fibre of the specified stabilization beta_B:F_A→Map(B,K(Z/2,2)); geometric H2 relative-cylinder obstruction',
        'remaining':'Evaluate F_A and beta_B; determine separate cokernel on original concordance components; higher PL-SA and general base-three gates remain',
        'original_A1b_complete':False,'early_progress_review_conducted':False,'finite_counterexample_claimed':False}
receipt.write_text(json.dumps(record,indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A.136\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: complete proof, original compact-bundle footnote, mixed-structure collars, strict pullback before boundary classification, ambient-five Kan restriction, cofinal top germs, natural stabilization, all based components and relative tangent homotopy; original component cokernel retained.\n')
    f.write('A.136\t'+now+'\tGPT-6 Astra, inherited configuration, higher_comparison2\ttargeted proof check\tPASS: independent complete audit with exact originals and explicit inverse for tangent microbundle homotopy; zero-section wording corrected and all original-component limitations retained.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A.136 integrated — '+now+'\n\n'
       'For every closed compact real PL four-manifold B, the entire based PL-to-TOP concordance comparison fibre is now the homotopy fibre of a specified stabilization map beta_B:F_A→Map(B,K(Z/2,2)), where F_A is the ordinary four-manifold automorphism comparison fibre. The construction is looped product with a line on sliced PL structures and open-five-dimensional classification, with its chosen standard PL lift. The component obstruction is the relative cylinder PL-structure class in H2(B;Z/2). Root and independent full audits passed.\n\n'
       'Unlike the preceding fibre sequence alone, this theorem specifies its extension map. The remaining based-comparison problem is to evaluate F_A and beta_B. The separate cokernel on original concordance components is not captured and remains unchanged; no parent task is marked complete. The scheduled review will assess this proved reduction against its baseline. This integration note is not an early review and does not itself reset the stopping count.\n')
print(json.dumps(record,indent=2))
