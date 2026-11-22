#!/usr/bin/env python3
"""Integrate the fully audited support-localized ordinary-loop theorem."""
from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parents[1]
out=root/'logs/A141_root_integration.json'
if out.exists():
    raise SystemExit('A141 integration already recorded')
proof='agents/higher_comparison/part_support_localized_four.tex'
audits=['notes/root_A141_support_localization_audit.md',
        'agents/singularities_duality/logs/support_localized_four_loop_independent_audit.md']
s=(root/proof).read_text()
assert s.count(r'\begin{saresult}{A.141}')==1 and r'\!left' not in s
for name in audits:
    assert (root/name).exists()
p=root/'parts/part_A.tex'
s=p.read_text()
anchor=r'\input{agents/singularities_duality/part_four_obstruction_realization}'
addition=r'\input{agents/higher_comparison/part_support_localized_four}'
assert s.count(anchor)==1 and addition not in s
p.write_text(s.replace(anchor,anchor+'\n'+addition))
p=root/'parts/unchecked_A.tex'
s=p.read_text()
anchor='vanishing only through degree three; the general base gate remains.\n'
addition=('A.141 further evaluates $J_B$ by ordinary loops supported in a\n'
          'compact simply connected codimension-zero submanifold $W$:\n'
          'its image contains the extension-by-zero image of\n'
          '$H^2(W,\\partial W;\\mathbb Z/2)$. If $H_2(W;\\mathbb Z/2)\n'
          '\\to H_2(B;\\mathbb Z/2)$ is onto, then $J_B$ is all\n'
          '$H^2(B;\\mathbb Z/2)$ and the PL component image is exactly\n'
          '$I_B$. This includes $B=C\\#D$ with $C$ simply connected\n'
          'and $H_2(D;\\mathbb Z/2)=0$, without an assembly hypothesis\n'
          'on $\\pi_1(B)$. The endpoint-isotopic-to-PL condition remains.\n')
assert s.count(anchor)==1
p.write_text(s.replace(anchor,anchor+addition))
p=root/'code/update_report.py'
lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        line=line.replace('A.119–A.140|','A.119–A.141|')
        anchor='and safe S4 vanishing only through degree3.'
        addition=(' A.141 realizes the extension-by-zero H2 cohomology of a simply connected '
                  'codimension-zero W by ordinary supported loops. If H2(W)→H2(B) is onto, '
                  'then J_B is all H2 and the PL component image equals I_B. This includes '
                  'C#D with C simply connected and H2(D;Z2)=0, with no assembly hypothesis '
                  'on pi1(B); the endpoint condition remains.')
        assert anchor in line
        lines[i]=line.replace(anchor,anchor+addition)
p.write_text('\n'.join(lines)+'\n')
now=datetime.now(timezone.utc).isoformat()
record={'statement':'A.141','recorded_utc':now,'where_proved':proof,'audits':audits,
        'proved':'Ordinary loops realize the supported relative H2 cohomology; surjective H2 inclusion evaluates J_B and reduces the component image to the endpoint condition',
        'remaining':'General endpoint predicate, full automorphism/stabilization comparison and general base3 gate',
        'original_task_status_changes':[],'early_progress_review_conducted':False}
out.write_text(json.dumps(record,indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A.141\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: full relative-boundary proof, correct H2(W,∂W), trivial action by duality, exact OPR suspension, ordinary GGHKP path, explicit spatial/time collars, zero-extension naturality, connected-sum calculation and retained endpoint condition.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A.141 integrated — '+now+'\n\n'
        'Ordinary TOP loops supported in a compact simply connected codimension-zero PL4 submanifold W realize its extension-by-zero relative H2 cohomology inside the closed base B. If H2(W)→H2(B) is onto, J_B is all H2 and the PL concordance component image is exactly the endpoint-admissible subgroup I_B. This applies to C#D with C simply connected and H2(D;Z2)=0, including C#k(S1xS3), without an assembly hypothesis on the ambient group. The proof has root and independent full audits.\n\n'
        'The endpoint predicate and whole-space comparison remain. This subgroup evaluation does not close an original row and does not automatically reset the stopping count. Only the next scheduled review will assess whether the remaining original gate has strictly narrowed.\n')
print(json.dumps(record,indent=2))
