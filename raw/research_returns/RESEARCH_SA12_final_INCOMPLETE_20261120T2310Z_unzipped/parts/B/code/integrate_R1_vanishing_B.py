#!/usr/bin/env python3
"""Integrate the checked first direct-image vanishing theorem.

Document maintenance only; not a mathematical computation.
"""
from pathlib import Path
import csv
import datetime
import json
import time

started = time.perf_counter()
base = Path(__file__).resolve().parents[1]
paper = base / 'paper_B.tex'
text = paper.read_text()
assert 'Statement L6c ' not in text, 'Already integrated'
marker = '% Checked support lemma for Part B; not included in paper_C.tex.'
assert text.count(marker) == 1
text = text.replace(marker, (base / 'L6_R1_vanishing.tex').read_text()+'\n\n'+marker)
text = text.replace('Lead L6: deformation theory and low-dimensional checks',
                    'Lead L6: deformation theory and direct-image vanishing')
text = text.replace('step whenever the extra $H^2$-injectivity assumption holds.',
                    'step; L6c below proves that its $H^2$-injectivity\nassumption holds automatically in every dimension.')
paper.write_text(text)

table = base / 'results_B.csv'
with table.open() as stream:
    reader = csv.DictReader(stream)
    fields = reader.fieldnames
    rows = list(reader)
assert fields is not None and len(fields) == 7
rows.append(dict(
    id='L6c',
    statement='R1f_*O_X vanishes for every proper birational normal-to-regular morphism of integral Noetherian schemes in characteristic p',
    status='Proved', where_proved='paper_B.tex Statement L6c',
    depends_on='B.1b; Marrama2026 Proposition3 and Theorem6; strict henselization; alpha_p and Artin-Schreier exact sequences; semilinear stable-span lemma',
    manuscript_pages='29/071-075',
    notes='All dimensions and arbitrary residue fields; no perfectness or field-base assumption. H1 isomorphism and H2 injection follow. The proof does not assert higher Ri vanishing or resolve the singular-target B2 image gate.'))
for row in rows:
    if row['id'] == 'L6a':
        row['notes'] = 'The H2 hypothesis is now verified in every normal-to-regular characteristic-p case by L6c; the general formal criterion remains separately useful.'
with table.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

with (base / 'CHECK_EVENTS_B.tsv').open('a') as stream:
    stream.write('L6c\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b\tindependent re-proof\tLocalized a hypothetical coherent R1 at a minimal support prime and strict-henselized; alpha_p and constant Z/p purity force injective Frobenius and no fixed vectors on a finite-length module. Injectivity kills the maximal-ideal action; stabilized semilinear spans and the finite etale Lang kernel force a nonzero fixed vector, a contradiction.\n')
    stream.write('L6c\t2026-11-20\tGPT-6 Astra (OpenAI), /root, independent reading of /root/part_b proof\ttargeted proof check\tRoot audited the finite-length Frobenius argument, stable-span correction over imperfect separably closed residue fields, finite etale degree p^r, alpha_p and Artin-Schreier comparisons. The source scope was then rechecked in Marrama Proposition3 and Theorem6. No gap found.\n')
    stream.write('L6c\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_c, independent reading of /root/part_b proof\ttargeted proof check\tC separately audited both the imperfect-field semilinear lemma and the localization/strict-henselization/torsor-purity steps, including normality under ind-etale base change and flat coherent cohomology. No gap found.\n')

with (base / 'corrections_B.tsv').open('a') as stream:
    stream.write('B-C08\tupload/PROMPT(20261120-001029).md\t136-139\t29/071-075\tL6 proposes a counterexample route in dimension at least3 with nonzero R1f_*O_X\tThe vanishing R1f_*O_X=0 holds in all dimensions for proper birational normal-to-regular maps in characteristic p, even over general Noetherian bases; thus this route has no instance.\tL6c; primary Marrama2026 Proposition3 and Theorem6\n')

with (base / 'notes.md').open('a') as stream:
    stream.write('\n## 2026-11-20 after checkpoint04: all-dimensional R1 vanishing\n\nL6c is proved and independently audited by root and C. The proof uses only the already checked torsor equivalence B.1b, applied to alpha_p and constant Z/p after strict henselization at a minimal support prime. A hypothetical R1 becomes finite length; injective Frobenius forces the maximal ideal to kill it. The necessary semilinear fixed-vector lemma is proved over separably closed imperfect residue fields by stabilizing the spans of F^n M before using an invertible matrix. This rules out the proposed nonzero-R1 route to a B.1 counterexample in every dimension and makes the formal criterion L6a automatic. It does not by itself improve the remaining dimension-at-least3 singular-target image gate in B.2.\n')

with (base / 'sources' / 'search_log.md').open('a') as stream:
    stream.write('\n### 2026-11-20 03:07--03:17: first direct-image vanishing\n\nRe-read Marrama2026 primary text Proposition3 p432 and Theorem6 pp433--434: locally Noetherian normality suffices for full faithfulness, and every regular base with codimension-at-least2 complement admits finite-flat torsor purity. No perfectness or field-base hypothesis occurs. Opened Stacks06DI (normality under strict henselization),06LN (regularity),02KE Lemma30.5.2 (flat cohomology base change),03DW Proposition35.9.3 (quasi-coherent cohomology independent of fppf/Zariski topology). These exact locators support L6c. Lipman1969 local full PDF download completed before03:07:28,9460787bytes,86pages; pdfinfo validated it.\n')

record = dict(operation='integrate_R1_vanishing_B',
              utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              statements=['L6c'], independent_audits=['root', 'part_c'],
              elapsed_seconds=time.perf_counter()-started)
(base / 'code' / 'output' / 'integrate_R1_vanishing_B.json').write_text(
    json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
