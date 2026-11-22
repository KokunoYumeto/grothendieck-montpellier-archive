#!/usr/bin/env python3
"""Integrate the audited low-dimensional comparison and retain the exact gates."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root = Path(__file__).resolve().parents[1]
receipt = root / 'logs/A134_root_integration.json'
if receipt.exists():
    raise SystemExit('A134 integration already recorded')
source = root / 'parts/parametric_concordance.tex'
text = source.read_text()
marker = r'\begin{saresult}{A.134}'
assert text.count(marker) == 1
head, body = text.split(marker)
destination = root / 'agents/singularities_duality/part_low_dim_TOP_comparison.tex'
assert not destination.exists()
destination.write_text('% AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).\n'
    + r'\subsection{Real comparison in base dimensions at most two}' + '\n\n'
    + marker + body)
source.write_text(head.rstrip()+'\n')
p = root / 'parts/part_A.tex'
text = p.read_text()
anchor = r'\input{agents/higher_comparison/part_elementary_extensions}'
assert text.count(anchor) == 1
p.write_text(text.replace(anchor, anchor+'\n'+r'\input{agents/singularities_duality/part_low_dim_TOP_comparison}'))

p = root / 'agents/singularities_duality/results.csv'
with p.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    records = list(reader)
matches = 0
for row in records:
    if row['id'] == 'A.134':
        row['where_proved'] = 'agents/singularities_duality/part_low_dim_TOP_comparison.tex A.134'
        matches += 1
assert matches == 1
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)

p = root / 'code/update_report.py'
lines = p.read_text().splitlines()
for i, line in enumerate(lines):
    if line.startswith('A.1(b)|'):
        lines[i] = ('A.1(b)|Unsettled; whole PL/SA models, low-dimensional TOP models and a refuted unrestricted comparison|'
          'A.103,A.113–A.116,A.119–A.134|'
          'A.131 gives complete effective countable simplicial-group models for the entire PL and semialgebraic concordance spaces in every dimension over every real closed field. Valid finite integer codes and equality are decidable, all structure operations are total algorithms, and the full Moore quotient gives recursive presentations of every homotopy group. A.113 identifies the PL component presentation with the definable component group in every fixed o-minimal expansion. A.134 proves the natural real PL-to-TOP weak equivalence for every closed base of dimension at most two, including mixed finite components and the empty base. Together with the comparison in base dimensions at least five, this supplies the same whole TOP model whenever every component has dimension outside three and four. A.132 refutes unrestricted PL-to-TOP weak equivalence: for the standard three-sphere PL pi2 is zero and TOP pi2 is Z/2, with the proved full TOP model Omega(TOP(4)/O(4)). The general real comparison now remains only in base dimensions three and four. A.133 proves whole-space invariance under elementary extension in one fixed o-minimal language, and transfers comparison properties across models of a complete theory, with a real-model corollary only when one exists. Higher PL-to-SA/arbitrary-definable comparison remains unsettled. In dimensions at least five PL-to-SA is injective in every degree and an isomorphism on components and pi1; real pi2 surjectivity, already for T6, is the first higher gate in that range. These exhaustive countable models are not finite classical invariant decompositions or terminating isotopy decisions. The countable-model corollary for arbitrary expansions is not a decidable or oracle-free effective computation. Earlier structural component and stable models retain their stated scopes.')
    if line.startswith('A.5 proper-map maximal locus and recursion|'):
        lines[i] = line.replace('A5.012–A5.014|','A5.012–A5.015|') + (' A5.015 gives a smooth proper polynomial global product with closed sphere fibres and no finite ambient Thom stratification; it refutes a proposed method criterion, while leaving this original gate unchanged.')
p.write_text('\n'.join(lines)+'\n')

p = root / 'parts/unchecked_A.tex'
text = p.read_text()
old = ('at least five the PL model also computes the real TOP space by the\n'
       'proved weak comparison. Thus the formerly separate effective\n')
new = ('at least five the PL model also computes the real TOP space by the\n'
       'proved weak comparison. A.134 now proves the same natural comparison\n'
       'for every closed base of dimension at most two, including all finite\n'
       'mixed-dimensional and empty cases. Thus the formerly separate effective\n')
assert old in text
text = text.replace(old, new)
text = text.replace('definable families, and the full real PL-to-TOP comparison in low base\ndimensions.',
    'definable families, and the general real PL-to-TOP comparison in base\ndimensions three and four.')
p.write_text(text)

p = root / 'agents/lie_theory/unchecked_A5.tex'
text = p.read_text()
text += ('\nA5.015 gives a proper polynomial global product with smooth algebraic\n'
         'source and closed sphere fibres that admits no finite ambient Thom\n'
         '$a_f$ stratification near its central axis. It refutes the proposed\n'
         'necessity of such a stratification for local bundle recognition.\n'
         'Its own maximal bundle locus is the whole base, so the original\n'
         'definability gate above remains unchanged.\n')
p.write_text(text)

now = datetime.now(timezone.utc).isoformat()
record = {
    'statement':'A.134', 'recorded_utc':now,
    'where_proved':str(destination.relative_to(root)),
    'root_audit':'notes/root_A134_low_dimension_audit.md',
    'independent_audit':'agents/higher_comparison/Hamstrom_surface_comparison_audit.md',
    'main_A1b_complete':False,
    'old_general_real_comparison_gate':'Base dimensions below five',
    'new_general_real_comparison_gate':'Base dimensions three and four; S3 full TOP model and pi2 discrepancy separately proved',
    'retained_other_gate':'Higher PL-to-SA and arbitrary fixed o-minimal comparison',
    'finite_counterexample_claimed':False
}
receipt.write_text(json.dumps(record,indent=2)+'\n')
with (root/'notes/root_checks.tsv').open('a') as f:
    f.write('A.134\t'+now+'\tGPT-6 Astra, inherited configuration, root\ttargeted proof check\tPASS: full proof, exact joint-family convention, TOP identity-component repair, bottom-setwise product splitting, annulus evaluation, TOP boundary correction, parameterized Alexander and finite/empty products checked against opened originals.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n### A.134 integrated — '+now+'\n\n'
       'The natural real PL-to-TOP concordance comparison is a weak equivalence for every closed base of dimension at most two. The proof handles the identity-component convention explicitly, uses a literal bottom-setwise product splitting for all closed surfaces, and proves the circle, point, finite mixed-dimensional and empty cases. The complete root and independent audits passed after the exact original Hamstrom, Scott, Yagasaki, Laudenbach and Epstein passages were opened.\n\n'
       'With A.131 this computes the whole TOP model in these dimensions. Together with the earlier base-at-least-five comparison, the general real comparison is now confined to base dimensions three and four; A.132 already gives the full S3 TOP model and its pi2 discrepancy. Higher PL–SA/arbitrary-definable comparison remains a separate gate. The scheduled review will assess this strict reduction against the original main-question criterion; this integration entry does not itself conduct an early review.\n')
print(json.dumps(record,indent=2))
