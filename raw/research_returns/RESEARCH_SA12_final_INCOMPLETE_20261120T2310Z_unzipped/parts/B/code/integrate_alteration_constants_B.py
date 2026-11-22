#!/usr/bin/env python3
"""Integrate the independently audited arbitrary-constant kernel reduction.

Document maintenance only, not a mathematical computation.
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
assert 'Statement B.2m ' not in text, 'Already integrated'
text += '\n\n' + (base / 'B2_alteration_constants.tex').read_text()
paper.write_text(text)

table = base / 'results_B.csv'
with table.open() as stream:
    reader = csv.DictReader(stream)
    fields = reader.fieldnames
    rows = list(reader)
assert fields is not None and len(fields) == 7
rows.append(dict(
    id='B.2m',
    statement='Over arbitrary k a fixed alteration after finite constants supplies a fixed Weil-restriction comparison and degree-bounded Picard kernel',
    status='Proved',
    where_proved='paper_B.tex Statement B.2m',
    depends_on='B.1g over l; B.2d and B.2j; deJong1997; Stacks01ZM/05Y8; universal base-line-bundle trivialization',
    manuscript_pages='29/075',
    notes='l/k may be inseparable; all nonreduced test schemes included. Root and C independently audited. No full tau-Weil-restriction identification or image bound asserted.'
))
with table.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

bib = base / 'references_B.bib'
text = bib.read_text().replace(
    '01ZM, 038O and 038P, including proofs.',
    '01ZM, 038O, 038P and 05Y8, including proofs.')
bib.write_text(text)

with (base / 'CHECK_EVENTS_B.tsv').open('a') as stream:
    stream.write('B.2m\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b with /root/part_c kernel simplification\tindependent re-proof\tExtended the fixed-alteration kernel bound to smooth alterations over arbitrary finite constants by an explicit generator-open fppf trivialization; used a fixed Weil restriction and avoided identifying tau over a non-geometrically-reduced k-source.\n')
    stream.write('B.2m\t2026-11-20\tGPT-6 Astra (OpenAI), /root, independent reading of /root/part_b proof\ttargeted proof check\tRoot checked normal l-graphs, all-parameter frame-torsor trivialization, separated Weil restriction and the Jacobian rank bound. Required and verified the correction to alteration over kbar followed by descent to a general finite l/k.\n')
    stream.write('B.2m\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_c, independent reading of /root/part_b proof\ttargeted proof check\tC checked the exact written proof: finite-constant issue corrected; determinant generator open smooth and surjective on every Artin geometric fibre; universal H0 and Leray; separated diagonal; degree annihilation and finite-rank descent. No gap found.\n')

with (base / 'unresolved_B.tex').open('a') as stream:
    stream.write(r'''

Statement B.2m removes the need for a geometrically integral
regular alteration over $k$ itself.  An alteration smooth over a
finite extension $l/k$ yields the fixed comparison
$\operatorname{Res}_{l/k}(\operatorname{Pic}^{\tau}_{Y/l})$;
the same degree and Jacobian bounds apply to its kernels.
The relative-base change is handled on all test schemes by
trivializing a line bundle on $T_l$ over an explicit smooth
surjective cover of $T$.  This also leaves only the image problem.
''')

with (base / 'notes.md').open('a') as stream:
    stream.write('\n## B.2m integrated at 2026-11-20 02:57 UTC\n\nThe fixed-alteration kernel bound is now unconditional on the constant field of an alteration: choose Y smooth geometrically integral over finite l/k by descent from kbar, compare through Res_{l/k}Pic^tau(Y/l), and use B.1g on normal main graphs over l. C simplified the proof to a kernel-only comparison, avoiding any tau/Weil-restriction equality. Root and C independently audited the complete written proof, including the correction from a potentially unjustified purely inseparable l/k to a general finite l/k. The remaining B.2-U gate is a uniform bound or realization of images in this fixed comparison object.\n')

with (base / 'sources' / 'search_log.md').open('a') as stream:
    stream.write('\n### 2026-11-20 02:53--02:57: arbitrary alteration constants\n\nOpened Stacks Section97.11, Tag05Y8, including Lemma97.11.2 (base change), Proposition97.11.5 (algebraic-space representability) and proofs. B.2m only requires the separated Weil-restriction sheaf; closedness of its diagonal is checked by coefficient equations. Existence of Y uses the already opened de Jong1997 alteration over kbar and finite-presentation descent, with no restriction on finite constants l/k.\n')

record = dict(operation='integrate_alteration_constants_B',
              utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              statement='B.2m',
              independent_audits=['root', 'part_c'],
              elapsed_seconds=time.perf_counter()-started)
(base / 'code' / 'output' / 'integrate_alteration_constants_B.json').write_text(
    json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
