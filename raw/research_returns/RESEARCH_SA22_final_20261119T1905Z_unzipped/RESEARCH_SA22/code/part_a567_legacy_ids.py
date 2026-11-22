#!/usr/bin/env python3
"""Retain exact supplied statement IDs for rechecks actually performed.

This is an audit crosswalk, not a rerun of mathematical proofs. The cited
proofs and finite certificates were completed in this run. Safe to rerun:
existing retained-ID audit events and lead result rows are not duplicated.
"""
from pathlib import Path
import csv

base=Path(__file__).resolve().parents[1]
incoming=base.parent/'inputs/RESEARCH_SA22_study/study/CHECK_EVENTS.tsv'
with incoming.open(newline='') as f:
    original={row['id']:(line,row) for line,row in enumerate(csv.DictReader(f,delimiter='\t'),2)}

checks={
'SA22-5 (67/050)':('A6-matrix-presentations','Proved','Both displayed presentations re-derived with completeness and exact matrix checks; not merely checked as relations.'),
'SA22-8 (67/084, extension of V and the standard form)':('A5-normalizer;A5-groupoid','Proved','Double transpositions extend uniquely; every Klein action is conjugate to the standard action, including characteristics3 and5.'),
'SA22-8 (67/084, normalizer and its sequence)':('A5-normalizer','Proved','Centralizer V and order24 normalizer re-derived; faithful face-pair action identifies it with S4 in every characteristic unequal to2.'),
'SA22-8 (67/085, splittings)':('A5-faces','Refuted and corrected','Single-face stabilizer is C3; an antipodal-face-pair stabilizer is S3 and complements V.'),
'SA22-8 (67/085-086, orientation and sqrt(-1))':('A5-normalizer;A5-faces','Proved','The two explicit normalizer generators are combinatorial rotations; replacing i by -i reverses orientation. Added full orientation verification after A5-faces.'),
'SA22-8 (67/086, Proposition)':('A5-six-points','Refuted and corrected','All-characteristic proof excludes exactly2 and5 for the unpaired-set claim; characteristic5 full stabilizer120 and exactlyfive Klein groups, with exhaustive certificate.'),
'SA22-8 (67/087, six-point V-sets)':('A5-normalizer;A5-groupoid','Proved','Each nonidentity element fixes its own pair and swaps the other two; the converse action is uniquely recovered from the three paired subsets. Detailed verification in notes.'),
'SA22-8 (67/088, quotient)':('A5-groupoid','Proved','The normalized quotient (z^2+1)^2/(4z^2) equals (q+2)/4 for the supplied q=z^2+z^-2; degree4 and all three branch fibers checked.'),
'SA22-8 (67/088, twisting; canonical model)':('A5-groupoid;A5-moduli','Proved','Contracted-product inverse, evaluation on the free fiber, full faithfulness, and family descent proved explicitly.'),
'SA22-8 (67/089, Theorem)':('A5-groupoid;A5-moduli','Proved with qualification','Groupoid theorem holds in every characteristic unequal to2. Earlier exceptional inertia orders8/12 need characteristic3 qualification: the loci merge at lambda=-1 with S4 inertia24; now explicit in A5.'),
"SA22-8 (67/086, '[reelle]')":('A5-normalizer','Scope checked; ink uncertainty retained','The algebraically closed base is rechecked. Tentative reelle is left uncertain and unused; no palaeographic certainty is asserted.'),
'SA22-9 (67/091-092, module equivalence)':('A7-gluing-modules','Proved','Explicit quasi-inverse and full faithfulness work for arbitrary two-torsion-free left modules over possibly noncommutative rings; no finiteness assumption.'),
"SA22-9 (67/091, Cor 'P, Q inv. de rg 1')":('A7-domain-counterexample','Refuted with stronger counterexample','Earlier connectedness repair is insufficient: the explicit integral-domain universal involution has a rank-one eigenspace with a two-dimensional residue fiber. Dedekind and two-invertible connected repairs proved.'),
'SA22-9 (67/100, conjugacy classes of involutions)':('A7-PID-count','Proved with corrected hypotheses','PID classification is residue units modulo global units. The -11 ring is proved norm-Euclidean, with F4 residue and three explicit nonsplit matrices; four classes total.'),
'SA22-9 (67/100, hexagonal reflection)':('A7-PID-count;A7-real-classification','Proved','On the hexagonal lattice conjugation sends u to u and w to u-w; matrix and generating lattice verified.'),
'SA22-9 (67/093, 099, families, periods, real points)':('A7-real-classification;A7-real-topology','Proved','Both period families, unique positive moduli, degree-two lattice inclusion, real automorphism groups and one/two real components re-derived.'),
'SA22-9 (67/094-095, 097-098, real structures on a given curve)':('A7-real-classification;A7-ratio-j','Proved','Exactlytwo real forms for real j, dihedral reflection classes, reciprocal moduli, square exception, and hexagonal parameters3 and1/3 proved.'),
'SA22-9 (67/093-101, the complete picture)':('A7-real-classification;A7-real-topology','Proved','Complete pointed and torsor classification supplied. The real j-ranges are now derived directly from real cubic discriminants, rather than adopted from memory.'),
"SA22-9 (67/097, 'serait-ce j = c log a ?')":('A7-ratio-j','Refuted','Reciprocal invariance and the square point a=1,j=1728 refute every proposed scalar multiple of log(a), without an unverified q-expansion.'),
'SA22-9 (67/101, torsors)':('A7-real-topology','Proved','Actual H1=H2(lattice) calculation gives Z/2 or0; explicit fixed-point-free cocycle, Klein quotient, and genus-one exhaustiveness proved. Restores sans bord mathematically.'),
'SA22-9 (67/091, sign in Q = Ker(id + sigma))':('A7-gluing-modules','Proved','Original091 image and transcribed sign checked in this run; anti-invariants are exactly Ker(id+sigma), as used in the full proof.'),
}
assert set(checks)<=set(original)
out=base/'checks/part_a567_input_id_map.csv'
with out.open('w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['original_id','current_ids','status','input_locator','actual_recheck'])
    for old,(new,status,reason) in checks.items():
        line,_=original[old]
        w.writerow([old,new,status,f'inputs/RESEARCH_SA22_study/study/CHECK_EVENTS.tsv:{line}',reason])

events=base/'checks/part_a567_events.tsv'
with events.open(newline='') as f:
    prior=list(csv.DictReader(f,delimiter='\t'))
seen={(r['statement_id'],r['type']) for r in prior}
event_type='retained input-ID recheck mapping'
with events.open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    for old,(new,status,reason) in checks.items():
        if (old,event_type) not in seen:
            w.writerow([old,'2026-11-19','GPT-6 Astra (OpenAI), part_a567, this run',event_type,f'{status}; maps to {new}. {reason}'])

leads=[
['L6','The anabelian sheets connect to later combinatorial anabelian geometry; exact modern answers require the stated logarithmic and arithmetic hypotheses','Known','sections/part_a6.tex','A6-anabelian; A6-procyclic; A6-cyclotomic-detection; A6-log-specialization; A6-canonical-compactification','67/048-051','Full modern source hypotheses checked; Nakamura1990 and Ihara-Nakamura1997 are not falsely marked as fully opened; opened1994/1995/2001 author accounts supply exact historical evidence'],
['L7','Theorem089 has a family realization as the unordered-four-point quotient stack, with separate coarse A1 and descent already over Z[1/2]','Proved under stated hypotheses','sections/part_a5.tex:A5-moduli','A5-groupoid; A5-moduli','67/084-089','Base, stack, coarse space, generic V inertia and characteristic3 exceptional S4 inertia distinguished'],
['L9','The real elliptic sheets recover the complete real lattice and genus-one torsor classification after the explicit algebraic and numerical corrections','Known','sections/part_a7.tex','A7-gluing-modules; A7-domain-counterexample; A7-PID-count; A7-real-classification; A7-real-topology','67/091-101','Alling connection checked against opened preview; formulas and exhaustiveness independently proved from opened uniformization and torsor theorems; rank-one corollary correction strengthened']]
results=base/'checks/part_a567_results.csv'
with results.open(newline='') as f: result_ids={r['id'] for r in csv.DictReader(f)}
with results.open('a',newline='') as f:
    w=csv.writer(f)
    for row in leads:
        if row[0] not in result_ids:w.writerow(row)
with events.open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    for row in leads:
        if (row[0],'lead status mapping') not in seen:
            w.writerow([row[0],'2026-11-19','GPT-6 Astra (OpenAI), part_a567, this run','lead status mapping',f'{row[2]}; maps to {row[4]}. {row[6]}'])
print(f'Retained {len(checks)} exact supplied statement IDs with actual rechecks and proof mappings.')
print('Added explicit status mappings for L6, L7 and L9.')
print('Unused date and palaeographic claims were not falsely marked as independently checked.')
