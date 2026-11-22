"""Record the checked finite-transcendence-degree arithmetic reduction."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

p = root/'parts/A/unresolved_A.tex'
s = p.read_text()
marker = 'The remaining gate is outside these classes.'
addition = r'''Corollary~\ref{A:A2-arithmetic-maximal} further proves A.2 for every noetherian characteristic-zero model with $\cd_p(K)=\operatorname{trdeg}_{\Q}K+2<\infty$, including every finitely generated characteristic-zero fraction field permitted in the question. The model need not be of finite type, normal or excellent. Among finite-transcendence-degree arithmetic fields, the residual gate therefore has cohomological dimension strictly below this maximal value. '''
if addition not in s:
    s = s.replace(marker, addition+marker)
    p.write_text(s)

p = root/'code/assemble.py'
s = p.read_text()
s = s.replace(
    'semilocal curves, arithmetic generic dimension two and specified local-surface/model classes proved',
    'semilocal curves, maximal arithmetic dimension and specified local-surface/model classes proved')
s = s.replace(
    'A:semilocal-Dedekind; A:A2-arithmetic-two; A:A2-local-surface',
    'A:semilocal-Dedekind; A:A2-arithmetic-two; A:A2-arithmetic-maximal; A:A2-local-surface')
s = s.replace(
    'A:Iwasawa-equivalence; A:A2-local-surface; A:strict-model-rigidity',
    'A:Iwasawa-equivalence; A:A2-arithmetic-maximal; A:A2-local-surface; A:strict-model-rigidity')
s = s.replace(
    'algebraic-number fraction fields of generic dimension two, specified nonexcellent local surfaces',
    'characteristic-zero fraction fields of maximal cohomological dimension trdeg_Q(K)+2 (in particular every finitely generated such field), specified nonexcellent local surfaces')
s = s.replace(
    "('L6','Full B.1 proved; formal criterion and surface case checked','B.1; L6a; L6b')",
    "('L6','Full B.1 proved; formal criterion and first direct-image vanishing in all dimensions proved','B.1; L6a; L6b; L6c')")
p.write_text(s)

events = root/'parts/A/CHECK_EVENTS_A.tsv'
with events.open('a', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['A:arithmetic-affine-relative', stamp,
        'GPT-6 Astra; inherited reasoning effort; /root',
        'targeted proof check',
        'Opened ILO XV Theorem1.1.2/reformulation1.2.1 p219; arithmetic duality input rechecked in Milne II.3. Flatness and dimension formula bound the induced dimension function by e+1. Highest direct image has generic stalk zero and cohomological dimension at most1, giving e+2 by Leray.'])
    w.writerow(['A:arithmetic-transcendence; A:A2-arithmetic-maximal', stamp,
        'GPT-6 Astra; inherited reasoning effort; /root',
        'targeted proof check',
        'Verified finite-type arithmetic approximation, arbitrary torsion coefficient limits, explicit nonreal shrink at p2, flat possibly nonintegral Gaussian quadratic cover, finite-cd descent, and the full hereditary affine-open quantifier.'])

supp = root/'report_supplement.md'
with supp.open('a') as f:
    f.write('''\n\n## Post-checkpoint04 arithmetic reduction\n\nThe proved arithmetic affine bound gives cd_p(R) at most trdeg_Q(Frac R)+2 for every characteristic-zero domain with p invertible when p is odd; for p=2 it gives this bound after the one explicit localization making a sum-of-squares expression for -1 regular. No Noetherian assumption is needed for the upper bound. Combining it with the generic lower witness proves A.2 for every Noetherian model of a finitely generated characteristic-zero field with finite p-cohomological dimension, and more generally every field attaining that maximal arithmetic dimension. This strictly removes these models from the residual A.2 gate. The cyclotomic dimension-one instance remains unresolved.\n\nThe derivation uses ILO, Expose XV, Theorem1.1.2 and reformulation1.2.1, p219, rather than assuming a fibrewise bound for a nonproper direct image. The top direct-image sheaf is supported at closed points of the arithmetic base, so it contributes one degree less to Leray. The quadratic cover at p2 is explicitly allowed to be reducible when the model is nonnormal. Searches for affine cohomological dimension over number rings and finite-type integer algebras were checked against the opened SGA4 and ILO statements; no priority is claimed.\n''')

with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write(f'''\n\n## Working update: {stamp} (not a scheduled formal review)\n\nA.2 has a further strict gate reduction: all Noetherian models of every finitely generated characteristic-zero fraction field of finite p-cohomological dimension are now covered, without finite type, normality or excellence of the model. More generally the arithmetic finite-transcendence-degree bound covers cd_p(K)=trdeg_Q(K)+2. The remaining finite-transcendence-degree arithmetic fields have a strict dimension drop, including the cyclotomic instance. The next formal review remains04:10 UTC, and no stopping review has been performed here.\n''')
print(json.dumps({'utc':stamp, 'new_A_statements':3,
                  'new_root_check_events':2, 'formal_review':False}))
