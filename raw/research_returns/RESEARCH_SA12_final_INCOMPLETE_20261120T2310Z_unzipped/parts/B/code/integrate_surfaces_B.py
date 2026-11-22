#!/usr/bin/env python3
"""Integrate the checked arbitrary-field surface upper-cone theorem.

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
assert 'Statement B.2n ' not in text, 'Already integrated'
text += '\n\n' + (base / 'B2_surfaces.tex').read_text()
paper.write_text(text)

table = base / 'results_B.csv'
with table.open() as stream:
    reader = csv.DictReader(stream)
    fields = reader.fieldnames
    rows = list(reader)
assert fields is not None and len(fields) == 7
rows.extend([
    dict(id='B.2n',
         statement='A proper birational morphism of geometrically normal proper surfaces with R1f_*O=0 induces an isomorphism on Pic^tau',
         status='Proved', where_proved='paper_B.tex Statement B.2n',
         depends_on='Lipman1969 Theorem12.1(i); L6a; closed Picard immersion; numerical triviality',
         manuscript_pages='29/075',
         notes='Geometric-point surjectivity is proved by local numerical descent; formal isomorphism retains all infinitesimal structure.'),
    dict(id='B.2o',
         statement='Weak upper-cone Picard stabilization holds for proper geometrically normal surface models over every field',
         status='Proved', where_proved='paper_B.tex Statement B.2o',
         depends_on='Lipman1978 resolution; Lipman1969 Proposition1.2(2); maximal length in fixed R1 sheaf; B.2n',
         manuscript_pages='29/075',
         notes='No filteredness or geometrically normal common refinement is assumed. Extends weak assertion to transcendence degree at most2; cofinal diagram remains separately formulated.')
])
for row in rows:
    if row['id'] == 'B.2-U':
        row['notes'] += ' Weak upper-cone assertion now proved in dimension at most2 by B.2o; remaining weak gate has dimension at least3.'
with table.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

with (base / 'references_B.bib').open('a') as stream:
    stream.write(r'''
@article{Lipman1969B,
  author = {Lipman, Joseph},
  title = {Rational singularities, with applications to algebraic surfaces and unique factorization},
  journal = {Publications Math\'ematiques de l'IH\'ES},
  volume = {36},
  pages = {195--279},
  year = {1969},
  doi = {10.1007/BF02684604},
  url = {https://www.numdam.org/item/PMIHES_1969__36__195_0.pdf},
  note = {Opened: full primary PDF, Definition1.1 and Proposition1.2(2), pp.199--200, and Theorem12.1(i) with proof, pp.220--221. All-field regular surface vanishing and numerical descent are used with their stated hypotheses. Accessed 2026-11-20}
}
''')

with (base / 'CHECK_EVENTS_B.tsv').open('a') as stream:
    stream.write('B.2n; B.2o\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b\tindependent re-proof\tUsed a fixed finite-length R1 sheaf on a regular surface resolution, maximal length and Leray to force R1=0 on an allowed upper cone; Lipman numerical descent plus formal Picard comparison gives full scheme isomorphisms.\n')
    stream.write('B.2n; B.2o\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_c, independent reading of /root/part_b argument\ttargeted proof check\tC independently opened Lipman1969 Definition1.1/Proposition1.2(2) pp199--200 and Theorem12.1(i) pp220--221; audited canonical R1 injections, maximal length, finite-support faithfulness, local descent, numerical triviality and completion argument. No gap found.\n')

with (base / 'unresolved_B.tex').open('a') as stream:
    stream.write(r'''

Statements B.2n--o now prove the weak upper-cone formulation
over every ground field for surfaces, and hence for transcendence
degree at most two.  The proof uses a maximal finite-length
subsheaf of the $R^1$ of one regular surface resolution and
Lipman's numerical descent theorem.  Its auxiliary common
regular resolutions need not be geometrically normal, so it
does not assume the disputed filteredness.  The remaining weak
upper-cone problem is therefore restricted to transcendence
degree at least three.  A stronger cofinal-diagram assertion
remains a separate question even in low dimension.
''')

with (base / 'notes.md').open('a') as stream:
    stream.write('\n## Surface reduction before checkpoint04\n\nB.2n--o establish the weak upper-cone Picard stabilization over arbitrary fields in dimension at most2. A fixed regular surface resolution gives a finite-length R1 sheaf; maximal length among permitted models forces R1=0 along the chosen upper cone. Lipman1969 Theorem12.1(i) provides geometric-point descent, and L6a plus the closed immersion retains the formal structure. C independently checked the source and proof. The proof uses regular-target vanishing from Lipman1969 Proposition1.2(2), not an unjustified application of the smooth CR2011 theorem over an imperfect field. The high-dimensional image bound and stronger cofinal formulation remain open.\n')

with (base / 'sources' / 'search_log.md').open('a') as stream:
    stream.write('\n### 2026-11-20 02:59--03:04: surface upper-cone argument\n\nOpened original Lipman1969 Numdam PDF https://www.numdam.org/item/PMIHES_1969__36__195_0.pdf. Read Definition1.1 and Proposition1.2(2), printed199--200, including the quadratic-transform proof; read Theorem12.1(i) and proof, printed220--221. The theorem assumes proper fibres of dimension at most1 and H1(O)=0 and says degree0 on every integral exceptional curve is equivalent to triviality over a local base. These locators are now used in B.2n--o. Full local PDF download is slow and is being resumed; opening/verification is complete through the primary web PDF.\n')

record = dict(operation='integrate_surfaces_B',
              utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              statements=['B.2n', 'B.2o'],
              independent_audit='part_c',
              elapsed_seconds=time.perf_counter()-started)
(base / 'code' / 'output' / 'integrate_surfaces_B.json').write_text(
    json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
