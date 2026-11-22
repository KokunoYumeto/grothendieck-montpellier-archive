#!/usr/bin/env python3
"""Idempotent manuscript/record integration preceding scheduled checkpoint06."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
p = root / 'RESEARCH_SA08_C3_D031_paper.tex'
s = p.read_text()
for anchor, new in [
    ('A_saturated_tail_H3', 'A_deep_tail_H2'),
    ('A_relative_period_repair', 'A_closed_boundary_cells'),
    ('A_uniform_tail_reduction', 'A_tail_inverse_limit'),
]:
    line = '\\input{sections/' + new + '}'
    if (root / 'sections' / (new + '.tex')).exists() and line not in s:
        old = '\\input{sections/' + anchor + '}'
        assert old in s
        s = s.replace(old, old + '\n' + line)
p.write_text(s)

fields = ['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
p = root / 'notes/A_deep_tail_results.csv'
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerow(dict(zip(fields, [
        'A-P01',
        'At every prime a specified degree-2p resolved-tail repair creates an exact order-p degree-two class surviving every based saturation stage, with an actual further projection-preserving repair',
        'Proved', 'sections/A_deep_tail_H2.tex A-P01',
        'Explicit coefficient resolution through p^2; A-SAT01; actual simplicial twists and detecting projection',
        '',
        'R=Z_(p), b>=3; witness weight 2pb+2p(p-1)+1. Actual source is partial; no counterexample to common admissible sources is inferred.'
    ])))

p = root / 'notes/A_root_CHECK_EVENTS.tsv'
with p.open(newline='') as f:
    old_events = list(csv.DictReader(f, delimiter='\t'))
new_events = [
    ('A-P01', 'independent re-proof', 'Full proof checked: exact alternating coefficient matrices and p^2 generator, complete low lattice, W truncation, nonzero exterior coefficient, entire saturation, actual twisted simplicial map and detecting augmentation, projection-preserving q2 repair.'),
    ('AT21', 'targeted proof check', 'Full written proof checked: actual degeneracy formula and every face, simultaneous inverse strict PD attachment maps and transport of specified target maps.'),
    ('AT21b', 'targeted proof check', 'Full algebraic transgression proof checked: K/L/D/E identities, specified edge relations, inverse resolved maps including W0, repair correction in the stated coefficient-resolution scope, and each based saturation stage.'),
    ('A-WF01', 'used and rechecked in this run', 'Read fetched arXiv v3 source: eta and alpha at lines588-605, saturation at678-692, completion at859-874, and Dieudonne algebra definition at1404-1413; matches the separately opened141-page author PDF definitions used in the calculation.'),
]
known = {(x['statement_id'],x['type'],x['outcome']) for x in old_events}
with p.open('a', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    for ident, typ, detail in new_events:
        if (ident,typ,detail) not in known:
            w.writerow([ident,'2026-11-19','GPT-6 Astra; root; RESEARCH_SA08_C3_D031',typ,detail])

p = root / 'notes/A_root_references.bib'
s = p.read_text().replace(
    'arXiv v3 source also requested.',
    'arXiv v3 source fetched and opened: crystalline-v3-submitted-to-journal.tex, lines588--605,678--692,859--874,1404--1413. Source archive SHA256 6d75a375457db2da2a5265a6080ea9e2a53b60eb04e3ed0ba7eb7c650ac221de.'
)
# Correct archive hash from the recorded fetch log, rather than a hand-copied value.
import json
log = json.loads((root/'logs/fetch_BLM1805_source.json').read_text())
def hashes(x):
    if isinstance(x,dict):
        for k,v in x.items():
            if k == 'sha256': yield v
            else: yield from hashes(v)
    elif isinstance(x,list):
        for v in x: yield from hashes(v)
h = next(hashes(log), None)
if h:
    s = s.replace('6d75a375457db2da2a5265a6080ea9e2a53b60eb04e3ed0ba7eb7c650ac221de', h)
p.write_text(s)

p = root / 'RESEARCH_SA08_C3_D031_report.md'
s = p.read_text()
marker = '| B: exact v4 statement and conventions |'
rows = '''| A: explicit relative quadratic repair | Proved | AT20 supplies reference forms, actual target maps and the next repair for the original closed-boundary cell, under all displayed source and target bounds. |
| A: general first odd-cell boundary | Proved | AT21 gives an explicit change of generators and its inverse over the free first skeleton; AT21b transports the resolved quadratic twist, chosen edges and subsequent repair in its stated scope. |
| A: low-degree defects at every prime | Proved | A-P01 constructs exact order-p H2 in weight 2pb+2p(p−1)+1 surviving all based saturation, and gives an actual next repair preserving the chosen projection. |
| A: weight Frobenius saturation | Refuted as the specified admissible replacement | A-WF01 computes the actual coefficient map: positive-weight H0 becomes rational, and the completed saturation kills the original positive-weight coefficients. |
'''
if '| A: explicit relative quadratic repair |' not in s:
    assert marker in s
    s = s.replace(marker, rows + marker)
program_rows = '''| A_cosimplicial_deep_tail_certificate.py | Complete coefficient lattices through p² for p=3,5, including e_(p²); 54 and250 exact local-lattice checks | 0.09312325301289093 |
| B_local_source_certificate.py | 84,058 checks, including2,159 coefficient-basis cases and9,525 normalized comparison-form cases | 0.3144910749979317 |
| B_cartier_translation_certificate.py | 609 exact checks for1–7 summands: integral K/L/D/E identities and final repair correction | 0.03568925301078707 |
'''
if '| A_cosimplicial_deep_tail_certificate.py |' not in s:
    assert '| B_source_audit.py |' in s
    s = s.replace('| B_source_audit.py |', program_rows + '| B_source_audit.py |')
heading = '\n## Additions checked for checkpoint06\n'
if heading not in s:
    s += heading + '''
The completed A-S09-24 reduction is now integrated in the main manuscript. Both main questions still have the same proper finite-degree gate C^[d]. No infinite-degree admissible completion follows from these tail functors.

AT20 handles the closed-boundary quadratic cell with its original target maps. AT21 constructs the boundary correction inside the existing second simplex using only actual degeneracies. AT21b gives the complete transgression formulas, prescribed edge values and inverse resolved maps; its subsequent degree-three comparison retains the exact coefficient-resolution scope stated in the proof. These results have been independently refereed, and their finite identities have a separate certificate.

A-P01 extends the previously detected degree-two defect to every prime. The proof includes the full low-weight coefficient resolution, including the generator at weight p², and the precise integral primitive lattice. It supplies an actual simplicial source and a detecting cochain map extending through every saturation stage. Its final attachment kills this class with the chosen projection, so the result records a repeated-repair problem rather than a disconnected pair of admissible theories.

The Bhatt–Lurie–Mathew saturation definitions were read both in the141-page author PDF and in the fetched arXiv v3 LaTeX source. A-WF01 computes the canonical weight Frobenius and both actual coefficient maps. It rules out this specified saturation/completion replacement; it does not claim a conclusion about an unspecified different Frobenius. Search queries and exact source locators are recorded in notes/A_frobenius_source_audit.md.
'''
p.write_text(s)
print('Integrated the available checkpoint06 sections and idempotent records.')
