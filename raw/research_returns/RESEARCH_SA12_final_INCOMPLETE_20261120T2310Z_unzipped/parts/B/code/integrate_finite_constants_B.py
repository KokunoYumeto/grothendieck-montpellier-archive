#!/usr/bin/env python3
"""Record the finite-constant-field corollary and opened related literature.

Document maintenance only; this program is not a mathematical certificate.
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
assert 'Statement B.2l ' not in text, 'Already integrated'
text += '\n\n' + (base / 'B2_finite_constants.tex').read_text()
marker = '\\subsubsection*{Statement B.1g '
assert marker in text
remark = r'''\begin{remark}[Related finite-group criteria]
For related criteria detecting finite-type commutative groups,
\cite[Lemmas 3.4.1--3.4.3, pp.~14--16 of the arXiv version]
{CotnerZavyalov2024B} establish lifting of primary torsion to
quotients, torsion-density statements in positive characteristic,
and an isomorphism criterion that also tests all finite $p$-power
group schemes.  Those statements likewise distinguish finite
connected subgroup schemes from their geometric points.  We have
given the finite-subgroup argument above with the hypotheses and
field descent needed for the present application.
\end{remark}

'''
text = text.replace(marker, remark + marker, 1)
paper.write_text(text)

table = base / 'results_B.csv'
with table.open() as stream:
    reader = csv.DictReader(stream)
    fields = reader.fieldnames
    rows = list(reader)
assert fields is not None and len(fields) == 7
rows.append(dict(
    id='B.2l',
    statement='For geometrically integral K/k, weak Picard stabilization holds after one finite purely inseparable extension of constants',
    status='Proved',
    where_proved='paper_B.tex Statement B.2l',
    depends_on='B.2h; Stacks01ZM/038O/038P; fpqc descent of isomorphisms',
    manuscript_pages='29/075',
    notes='No original-field descent or cofinality is asserted. The stable perfect-field model descends with its birational marking.'
))
with table.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

bib = base / 'references_B.bib'
text = bib.read_text().replace(
    '0BCY and 0BD2, including proofs.',
    '0BCY, 0BD2, 01ZM, 038O and 038P, including proofs.')
text += r'''
@article{CotnerZavyalov2024B,
  author = {Cotner, Sean and Zavyalov, Bogdan},
  title = {{Lefschetz} theorems in flat cohomology and applications},
  journal = {Compositio Mathematica},
  volume = {160},
  pages = {1850--1870},
  year = {2024},
  doi = {10.1112/S0010437X24007231},
  eprint = {2204.06121},
  archivePrefix = {arXiv},
  url = {https://arxiv.org/pdf/2204.06121},
  note = {Opened: arXiv v3 PDF and TeX, Lemmas 3.4.1--3.4.3, pp.14--16. Cited for related finite-group criteria, not for birational-model stabilization. Accessed 2026-11-20}
}
'''
bib.write_text(text)

with (base / 'CHECK_EVENTS_B.tsv').open('a') as stream:
    stream.write('B.2l\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b\tindependent re-proof\tDescended the stable projective model over the perfect closure together with its birational marking to finite purely inseparable constants; checked geometric normality via Stacks038O/038P and every dominating geometric-normal model by fpqc base change. No cofinality or descent to the original field is inferred.\n')

with (base / 'unresolved_B.tex').open('a') as stream:
    stream.write(r'''

Statement B.2l now establishes the weak upper-cone formulation
after one finite purely inseparable extension of the constants,
for geometrically integral $K/k$.  The model and its birational
marking descend from the perfect closure by finite presentation.
Thus the residual gate is descent to the original field and
realization of the required Picard image by an allowed model;
it is not the finite field-of-definition step.
''')

record = dict(operation='integrate_finite_constants_B',
              utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              statement='B.2l',
              added_reference='CotnerZavyalov2024B',
              elapsed_seconds=time.perf_counter()-started)
(base / 'code' / 'output' / 'integrate_finite_constants_B.json').write_text(
    json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
