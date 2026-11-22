#!/usr/bin/env python3
"""Integrate the independently checked C alteration-kernel proof into Part B.

This is a document-maintenance program, not a mathematical certificate.
It writes only inside parts/B and refuses duplicate integration.
"""
from pathlib import Path
import csv
import datetime
import json
import time

started = time.perf_counter()
base = Path(__file__).resolve().parents[1]
source = base.parent / 'C' / 'B2_norm_notes.tex'
fragment = source.read_text()
fragment = fragment.replace('C_StacksPicNorm', 'StacksB')
fragment = fragment.replace('C:B2-alteration-kernel', 'B:B2-alteration-kernel')
fragment = fragment.replace('C:B2-fixed-alteration-kernel', 'B:B2-fixed-alteration-kernel')
fragment = fragment.replace(
    r'\begin{lemma}[A degree bound for the alteration kernel]',
    r'\subsubsection*{Statement B.2j (Proved): a degree bound for alteration kernels}'
    '\n' + r'\begin{lemma}[A degree bound for the alteration kernel]')
fragment = fragment.replace(
    r'\begin{corollary}[Uniform kernel along a fixed alteration]',
    r'\subsubsection*{Statement B.2k (Proved): a uniform kernel along a fixed alteration}'
    '\n' + r'\begin{corollary}[Uniform kernel along a fixed alteration]')
paper = base / 'paper_B.tex'
text = paper.read_text()
assert 'Statement B.2j' not in text, 'Already integrated'
text += '\n\n' + fragment
paper.write_text(text)
(base / 'B2_norm_checked.tex').write_text(fragment)

table = base / 'results_B.csv'
rows = list(csv.DictReader(table.open()))
fields = list(rows[0])
rows.extend([
    dict(id='B.2j', statement='The fppf Picard-sheaf kernel of a proper normal generically finite map is killed by its generic degree',
         status='Proved', where_proved='paper_B.tex Statement B.2j',
         depends_on='Normal Stein factor; Stacks02KH/0EBJ/0BCY/0BD2; universal Hartogs',
         manuscript_pages='29/075',
         notes='Includes all nonreduced parameter schemes. Proof supplied by C and independently audited by B.'),
    dict(id='B.2k', statement='Along a fixed regular alteration of degree d, Picard pullback kernels for geometrically normal modifications have rank at most d^(2g)',
         status='Proved under stated hypotheses', where_proved='paper_B.tex Statement B.2k',
         depends_on='B.1g; B.2d; B.2j; fixed g-dimensional Jacobian torsion',
         manuscript_pages='29/075',
         notes='The source of the fixed alteration is regular and geometrically integral. This controls the kernel; the imperfect-field image gate remains separate.')
])
with table.open('w', newline='') as output:
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

bib = base / 'references_B.bib'
text = bib.read_text().replace(
    '0BXT and 0CCJ, including proofs.',
    '0BXT, 0CCJ, 02KH, 0EBJ, 0BCY and 0BD2, including proofs.')
bib.write_text(text)

events = base / 'CHECK_EVENTS_B.tsv'
with events.open('a') as output:
    output.write('B.2j; B.2k\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_c\tindependent re-proof\tDerived generic-degree annihilation of the full Picard-sheaf kernel using normal Stein factor, norm on the codimension-one flat locus, and Hartogs universally in parameter schemes; combined B.1g and B.2d for fixed-Jacobian rank bound.\n')
    output.write('B.2j; B.2k\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b, independent reading of /root/part_c proof\ttargeted proof check\tOpened Stacks02KH,0EBJ,0BCY,0BD2 and checked normality of Stein factor, generic degree, codimension-one local freeness, nonreduced-test-scheme Hartogs, fppf trivialization and rank bound. No gap found; no image bound inferred.\n')

unresolved = base / 'unresolved_B.tex'
text = unresolved.read_text()
text += r'''

Statements B.2j--k remove a separate obstruction in the alteration
approach.  A fixed regular geometrically integral alteration of generic
degree $d$ has pullback kernel killed by $d$ on the entire fppf Picard
sheaf; the fixed-Jacobian embedding bounds its rank by $d^{2g}$.
Normal graph modifications of that alteration have the same Picard
group by B.1g, even when the graph is not geometrically normal.
What remains is the image: we have not proved a uniform bound on
the finite quotients of these images over the image of one permitted
geometrically normal model.

Even a fixed abelian ambient group and a fixed tangent dimension do
not establish that image bound formally.  For an elliptic curve $E$
in characteristic $p$, the chain $\ker F^r_{E/k}$ consists of closed
finite subgroup schemes of $E$, has constant tangent dimension one,
and has strictly increasing ranks $p^r$
\cite[Proposition 2.29]{MilneAG2022B}.  This remains an abstract group
scheme illustration; we do not assert that this chain is realized by
the geometrically normal models in question.
'''
unresolved.write_text(text)

record = dict(operation='integrate_post03_B',
              utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              statements=['B.2j', 'B.2k'],
              status='integrated_after_independent_B_audit',
              elapsed_seconds=time.perf_counter()-started)
(base / 'code' / 'output' / 'integrate_post03_B.json').write_text(
    json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
