#!/usr/bin/env python3
"""Record the dated research changes since checkpoint 01 without repackaging."""
from pathlib import Path
import csv,json
ROOT=Path(__file__).resolve().parents[1]
changes={
 'A.3(c)':('Bare and unframed coherent claims proved; framed stronger claim refuted','A:enrichment;A:unframed-adelic','Prescribed adelic Artin restrictions are essential; arbitrary incoherent families are not included'),
 'A.5':('Proved in corrected form','A:unconditional;A:lefschetz;A:kisin','Independent signed Kisin and Honda–Tate checks completed'),
 'B.3':('Arithmetic claims refuted/corrected; regular finite-field equivalences proved; finiteness undecided','sec:B','Brauer/Jacobian equivalence includes nonproper regular bases and no section; arbitrary singular bases and universal finiteness remain separate gates'),
 'B.4':('Effective finite torsion presentations proved; primitive-generator audit continuing','sec:B;thm:B-effective-odd-torsion','All 2-primary terms explicit; odd-primary terms given by terminating arithmetic matrices; integral free-generator saturation under final audit'),
 'C.4':('Proposed bound refuted; corrected level bounds proved; one sharp-weight endpoint unresolved','sec:C','Uses inherited delta-dimension, not ordinary local Krull dimension; mixed-characteristic i=0 coefficient endpoint remains'),
 'C.6':('All abelian-type motives proved; general-motive task incomplete','c:ell-independence-abelian','Weak Mumford–Tate lift, potentially good generator and common finite inertia traces; no exact named-conjecture equivalence for general motives yet'),
 'D.1':('Literal bridges refuted; corrected determinations proved','sec:D','Schematic closure, rational gerbe morphism, twisting units, exact-residue CM lifting after a power; independent audit completed')
}
path=ROOT/'ITEM_STATUS.tsv'
rows=list(csv.reader(path.open(),delimiter='\t'))
for row in rows:
 if row and row[0] in changes:row[1:]=list(changes[row[0]])
with path.open('w',newline='') as f:csv.writer(f,delimiter='\t').writerows(rows)
report=ROOT/'RESEARCH_SA05_report.md';s=report.read_text();lines=s.splitlines()
for i,line in enumerate(lines):
 for item,(status,label,note) in changes.items():
  if line.startswith('| '+item+' |'):lines[i]=f'| {item} | {status} | {label} | {note} |'
s='\n'.join(lines)+'\n'
s=s.replace('### Last checkpoint audit update','### Checkpoint 01 historical audit update (03:35 UTC)')
s=s.replace('### Checkpoint PDF verification','### Checkpoint 01 PDF verification')
addition='''
## Changes after checkpoint 01

The Kisin sign comparison is now proved: his source gerbe uses the negative arithmetic fundamental class and his slope cocharacter is also negative. Inverting the source band identifies the conventions; the target Weil-number band is unchanged. The Honda–Tate local-index calculation in the explicit Lefschetz example has been independently checked.

For A.3(c), the paper now proves the unframed coherent adelic classification separately from the framed counterexample. Matching the prescribed Artin restrictions lifts the difference torsors to the connected band P. Milne's global-to-adelic H1 isomorphism supplies the global equivalence; its lift to H preserves the global Artin–Tate rigidification. There is no claim that arbitrary independent local choices satisfy the necessary adelic condition.

The odd-primary terms in the integral number-ring calculation now have a terminating finite arithmetic presentation. The proof includes a finite prime bound, an explicit discriminant and defining-polynomial bound, compact-support cocycle matrices, their Pontryagin duals, and a proved stopping criterion. The 2-primary groups and their generators are explicit. The primitive free-generator construction is separately audited; no conjectural uniform vanishing pattern is inserted into the table. The small finite-group program checks eight cyclic/S3 presentations in exact arithmetic; it does not run the enormous number-field enumeration. Its measured runtime is in `code/check_finite_cocycle_presentation_output.json`.

For C.6, all rational motives of abelian type are now covered, including arbitrary initial bad reduction and residue characteristic2. The proof changes the abelian generator using Noot's weak Mumford–Tate lift, proves potential good reduction, then returns to the original field by induction. Inertia acts through one finite quotient on the new ambient object. Its graphs are Lefschetz classes, so the October2026 rationality theorem gives common rational traces on every Hodge projector. Finite-order trace equal to dimension forces the identity. The argument does not assert full Weil–Deligne compatibility. The general-motive question remains incomplete.

The sharp level bounds in C.4 are proved with the inherited dimension function, including the margin's relative-dimension hypothesis. The strengthened bound stated in the prompt is false. The sharp mixed-characteristic weight endpoint for degree0 and nonconstant positive-weight coefficients remains an exact local-invariant-cycle gate. The general K3 all-powers Chow relation remains unproved. A withdrawn October2026 preprint on products of K3 surfaces is not used.

The canonical results index is now generated from every numbered statement in the TeX sources, including included subsections, with balanced-brace status parsing and compiled theorem numbers. The individual per-item ledgers are retained alongside it. This replaces the earlier mixed item/statement index; no mathematical assertion is dropped.
'''
if '## Changes after checkpoint 01' not in s:s+=addition
report.write_text(s)
ledger=ROOT/'PROGRESS_LEDGER.md'
with ledger.open('a') as f:f.write('''
## 04:12 UTC gate changes and source audit

A.3(c) now also has a proof for unframed coherent adelic systems with fixed Artin restrictions; the framed square-class obstruction is retained with its exact different scope. C.6's abelian-type task is closed using a potentially good generator and common finite-inertia traces. Its general-motive named-equivalence task remains open. B.4 now has explicit terminating finite presentations for all odd-primary C_n and a closed 2-primary formula; the primitive integral free-generator algorithm is under independent audit. Thus the B.4 gate is strictly smaller than an unspecified finite K-group. B.3's regular finite-field equivalences now include nonproper bases and curves without sections, but the universal finiteness decision is not inferred from an equivalence with Tate/BSD.

New failed approaches are recorded explicitly: the published Kerr–Yang general correction-cycle formulas cannot be used without closure checks, and a later Kerr–Li paper acknowledges nonclosure in a low-degree construction. The replacement uses the earlier existence theorem and a certified finite search, with actual denominators. The withdrawn K3 product preprint is excluded. Fontaine's full Weil–Deligne conjecture is a sufficient general C.6 hypothesis, but no unjustified converse is asserted.

This is an interim update, not the first scheduled three-hour review. Next checkpoint remains due04:20UTC; first formal review remains05:50UTC.
''')
events=[
 ('A:unframed-adelic','targeted proof check','Root and Part D checked the fixed-Artin reduction to P, Milne03 H1(Q,P)=H1(A,P), the lift H1(Q,H)→H1(Q,P), and the real morphism torsor.'),
 ('thm:B-effective-odd-torsion','targeted proof check','Part B independently audited the explicit prime/polynomial bounds, compact-support cocycle presentation, cohomological dimension and stopping criterion.'),
 ('thm:B-effective-odd-torsion','computation or formal certificate','Eight synthetic exact finite-group presentations pass; code/check_finite_cocycle_presentation.py and JSON. This is not an arithmetic enumeration.'),
 ('c:ell-independence-abelian','targeted proof check','Root opened the original rationality theorem and checked all-places good reduction, induction, graph Lefschetz classes, Kunneth signs and finite-order trace criterion.'),
 ('thm:B-primitive-generator','targeted proof check','Root checked FM pp1503–1505 eq88 and Prop5.35 against KY3.3,3.8: raw regulator and lattice normalization match; final independent audit remains before inclusion.')
]
fields=['statement_id','date','who','type','outcome']
target=ROOT/'ROOT_CHECK_EVENTS.tsv'
with target.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(fields)
 for ident,kind,outcome in events:w.writerow([ident,'2026-11-19T04:12:00Z','GPT-6 Astra / root / current run',kind,outcome])
print(json.dumps({'item_updates':list(changes),'new_root_events':len(events)}))
