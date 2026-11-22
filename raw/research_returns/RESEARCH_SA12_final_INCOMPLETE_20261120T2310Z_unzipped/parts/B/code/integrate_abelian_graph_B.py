#!/usr/bin/env python3
"""Integrate the audited elliptic-target graph counterexample (maintenance)."""
from pathlib import Path
import csv
import datetime
import json
import time

started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
paper=base/'paper_B.tex'
text=paper.read_text()
assert 'Statement B.2p ' not in text
paper.write_text(text+'\n\n'+(base/'B2_abelian_graph_counterexample.tex').read_text())

path=base/'results_B.csv'
with path.open() as stream:
    reader=csv.DictReader(stream)
    fields=reader.fieldnames
    rows=list(reader)
assert len(fields)==7
rows.append(dict(
    id='B.2p',
    statement='An abelian target does not ensure a geometrically normal graph or an allowed resolution over an imperfect field',
    status='Refuted with explicit counterexample and scoped replacement',
    where_proved='paper_B.tex Statement B.2p',
    depends_on='Explicit characteristic3 complete intersection; incidence ruled surface; codimension1 isomorphism; finite algebra certificate',
    manuscript_pages='29/075',
    notes='A projective geometrically normal surface maps rationally to an elliptic curve; its normal graph has a geometrically nonnormal exceptional divisor that no allowed refinement can retain. Does not refute weak Picard stabilization.'))
for row in rows:
    if row['id']=='B.2-U':
        row['notes'] += ' The previously proposed abelian-target geometric-normality lemma is now explicitly refuted by B.2p; a controlled realization or different image argument is needed.'
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields)
    writer.writeheader();writer.writerows(rows)

with (base/'CHECK_EVENTS_B.tsv').open('a') as stream:
    stream.write('L6c\t2026-11-20\tGPT-6 Astra (OpenAI), /root, actual-file reading\ttargeted proof check\tRoot read paper_B.tex1124--1249 after integration and audited the complete written vanishing proof, including schematic density, minimal support, both torsor sequences, imperfect-field stable spans and Leray. No gap found; no higher-Ri conclusion inferred.\n')
    stream.write('B.2p\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b\trefuted, with the refined statement\tConstructed the explicit projective surface F=0,V^3=aW^3+WQ and its incidence graph; proved geometric normality of the surface and codimension1 geometric nonnormality of the normal graph with elliptic target.\n')
    stream.write('B.2p\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_c\ttargeted proof check\tC independently checked integrality, complete-intersection S2, exact finite Jacobian locus, regularity of the Cartier quotient E_l at every point, incidence graph equality and codimension1 obstruction. No gap found; not a Picard stabilization counterexample.\n')
    stream.write('B.2p\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_d\ttargeted proof check\tD independently checked six simple Q zeros, W-adic irreducibility, finite singular locus, normality of the graph, cusp equation after base extension and impossibility of a geometrically normal resolving modification. No gap found.\n')
    stream.write('B.2p\t2026-11-20\tGPT-6 Astra (OpenAI), /root, actual-file reading\ttargeted proof check\tRoot read B2_abelian_graph_counterexample.tex and checked finite flat projection, valuation irreducibility, exact Jacobian locus, incidence and graph equality, Cartier regularity, integral cusp element and codimension1 persistence. No gap found; weak B2 remains separately scoped.\n')
    stream.write('B.2p\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b\tcomputation or formal certificate\tabelian_graph_certificate_B.py passed19 exact assertions over F3 and F729 using SymPy1.14.0 in0.179927067s. Initial harness attempts failed from unreduced coefficient handling and a mistyped cleared-denominator exponent; both were corrected before the successful retained certificate.\n')

path=base/'unresolved_B.tex'
text=path.read_text()
old='''One remaining avenue is to realize the rational Albanese on a
geometrically normal compactification: it would suffice to prove a
suitable geometric-normality assertion for the normalized graph of
a rational map from a geometrically normal proper variety to an
abelian variety, together with bounded descent for its finite
infinitesimal part.  We have not proved that graph assertion.
'''
new='''One attempted avenue was to realize the rational Albanese by taking
the normalized graph of a map to an abelian variety.  Statement B.2p
now refutes the geometric-normality assertion needed by that method,
even for a projective surface and an elliptic target.  It gives an
explicit obstruction to this construction, not a counterexample to
weak Picard stabilization.  A controlled realization that contracts
the offending divisorial valuations, or a different image argument,
is still required in higher dimension.
'''
assert old in text
text=text.replace(old,new)
text=text.replace('Neither replacement follows\njust from B.2i, and we are still investigating them.',
                  'Neither replacement follows\njust from B.2i.  The weak statement is proved in dimension at most\ntwo below; its higher-dimensional scope and the strong formulation\nremain under investigation.')
path.write_text(text)

with (base/'notes.md').open('a') as stream:
    stream.write('\n## 2026-11-20 03:26: explicit abelian-graph obstruction\n\nB.2p refutes the special abelian-target graph lemma. The counterexample is the characteristic3 complete intersection over F3(a) given explicitly in the checked paper. It has seven geometric singular points and is geometrically normal; its normal incidence graph is regular along an exceptional E_{k(a^(1/3))}, whose generic local ring becomes the cusp s^3=t^2q after extending constants. Any normal resolving modification must retain that divisorial valuation, which is incompatible with geometric normality. Root, C and D independently audited the construction; root also audited the actual written file. The exact19-assertion certificate passed. Two initial certificate-harness errors were corrected: coefficient reduction before a univariate Poly, and the exponent t^4 in the cleared-denominator identity s^6=t^4q^2. The proposed stronger threefold nonconstant-Picard-branch construction is being independently attacked by C and remains provisional.\n')

record=dict(operation='integrate_abelian_graph_B',
            utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            statements=['B.2p'],audits=['root_actual_file','part_c','part_d'],
            elapsed_seconds=time.perf_counter()-started)
(base/'code'/'output'/'integrate_abelian_graph_B.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
