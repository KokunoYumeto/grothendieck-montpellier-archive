"""Integrate the actual-file-audited topological-normalization A.2 results."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
paper = root / 'parts/A/paper_A.tex'
anchor = r'\input{parts/A/overrings_A2_post04.tex}'
addition = r'\input{parts/A/topological_models_A2_post05.tex}'
s = paper.read_text()
if addition in s:
    raise SystemExit('Refusing duplicate integration.')
assert anchor in s
paper.write_text(s.replace(anchor, anchor + '\n' + addition))

unresolved = root / 'parts/A/unresolved_A.tex'
s = unresolved.read_text()
anchor = 'The remaining gate is outside these classes.'
assert anchor in s
s = s.replace(anchor,
    r'Theorem~\ref{A:A2-topnormal-models} further covers every model with a geometrically unibranch dense open, and every semilocal noetherian model, of a quasi-excellent strictly local fraction field in every dimension. The normalization can be infinite and nonnoetherian; the finite topological-normalization step is justified by EGA. The remaining gate is outside these classes.')
unresolved.write_text(s)

bib = root / 'parts/A/references_A.bib'
s = bib.read_text()
s = s.replace('note = {Opened: Tag 00PG,',
    'note = {Opened: Tag 0GIQ, Lemma 29.55.12, on normalization of geometrically unibranch schemes; Tag 04DZ, Theorem 59.45.2, on topological invariance of the small etale site for integral universal homeomorphisms; Tag 00PG,')
s = s.replace('Opened: full original French PDF; Chapitre 0, Proposition 23.2.7',
    'Opened: full original French PDF; Chapitre 0, Theorem 23.1.5, Proposition 23.2.4 and Corollary 23.2.5, printed pp. 215--219, for the finite topological normalization of semilocal models; also Proposition 23.2.7')
bib.write_text(s)

results = root / 'parts/A/results_A.csv'
with results.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
new = [
    ('A:semilocal-topnormalization', 'Finite topological normalization of every semilocal Noetherian domain, followed by one principal localization', 'Known with stated semilocal derivation', 'A_EGAIV1:0.23.1.5,0.23.2.4(ii),0.23.2.5'),
    ('A:strict-overring-bound', 'cd_p(T)≤dim(B) for every B⊂T⊂Frac(B), with B quasi-excellent strictly henselian Noetherian and p invertible', 'Proved', 'A:relative-affine; A:A2-approximation'),
    ('A:A2-topnormal-models', 'A.2 for every semilocal model or model with a geometrically unibranch dense open of a quasi-excellent strictly local fraction field', 'Proved under stated hypotheses', 'A:semilocal-topnormalization; A:strict-overring-bound; A:strict-normalization-rigidity; A:spread')
]
for label, statement, status, dependencies in new:
    assert not any(r['id'] == label for r in rows)
    rows.append(dict(zip(fields, [label, statement, status,
        'parts/A/topological_models_A2_post05.tex: label ' + label,
        dependencies, '31/085, Conjecture 3',
        'Actual-file independent audit by Part C and root; no finite-normalization or normal-model hypothesis.'])))
with results.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

events = root / 'parts/A/CHECK_EVENTS_A.tsv'
with events.open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    labels = '; '.join(x[0] for x in new)
    writer.writerow([labels, now.strftime('%Y-%m-%d %H:%M UTC'),
        'GPT-6 Astra; inherited reasoning effort; /root', 'targeted proof check',
        'Opened EGA0.23.2.4–5 and 0.23.1.5, Stacks0GIQ and04DZ. Checked finite product faithful flatness, Japanese complete-domain quotients, the finite birational denominator localization, all-coefficient overring continuity without Noetherianity, each affine subopen, and d=0.'])
    writer.writerow([labels, now.strftime('%Y-%m-%d %H:%M UTC'),
        'GPT-6 Astra; inherited reasoning effort; /root/part_c', 'independent re-proof',
        'Read actual topological_models_A2_post05.tex and the EGA source. Independently checked all three written results, infinite normalization and field-extension sites, and the exact hereditary A.2 quantifiers. No mathematical correction required.'])

ledger = root / 'PROGRESS_LEDGER.md'
ledger.write_text(ledger.read_text() + '\n\n## Working update: '
    + now.strftime('%Y-%m-%d %H:%M UTC')
    + ' (not a scheduled formal review)\n\n'
    'A.2 is now proved for every semilocal Noetherian model of a quasi-excellent '
    'strictly local fraction field, in every dimension and without normality. '
    'The same argument covers every model with a geometrically unibranch dense '
    'open. EGA finite topological normalization plus one localization and '
    'all-coefficient overring approximation supply the comparison. The full '
    'written fragment received an independent actual-file audit. This removes '
    'additional nonnormal higher-dimensional cases from the residual gate. '
    'Formal review02 remains due04:10 UTC; no stopping review is performed here.\n')

assembler = root / 'code/assemble.py'
s = assembler.read_text()
s = s.replace('all models of specified local-surface fields proved; exact cyclotomic Iwasawa instance',
    'all models of specified local-surface fields and semilocal/topologically normal strict-field models proved; exact cyclotomic Iwasawa instance')
s = s.replace('A:strict-model-rigidity; A:canonical-Iwasawa',
    'A:strict-model-rigidity; A:A2-topnormal-models; A:canonical-Iwasawa')
s = s.replace('and normal models of quasi-excellent strictly local fraction fields.',
    'and all semilocal models or models with a geometrically unibranch dense open of quasi-excellent strictly local fraction fields.')
assembler.write_text(s)

report = root / 'report_supplement.md'
with report.open('a') as f:
    f.write('\n\n## Post-checkpoint05 topological normalization comparison\n\n'
        'The three statements in parts/A/topological_models_A2_post05.tex extend '
        'A.2 to nonnormal semilocal models in all dimensions and to models with '
        'a geometrically unibranch dense open, for the specified quasi-excellent '
        'strictly local fraction fields. EGA IV1, Chapter0, Proposition23.2.4(ii) '
        'and Corollary23.2.5 were opened and the exact semilocal derivation '
        'checked. A separate actual-file audit verified that infinite '
        'normalization and arbitrary torsion coefficients are retained. '
        'The result does not assert the existence of such an open on every '
        'Noetherian model.\n')
print(json.dumps({'utc': now.isoformat(), 'added_statements': len(new),
    'fragment': 'parts/A/topological_models_A2_post05.tex'}))
