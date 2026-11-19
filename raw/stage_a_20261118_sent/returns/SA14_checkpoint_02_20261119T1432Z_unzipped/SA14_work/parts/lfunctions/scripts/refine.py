from pathlib import Path
p=Path('SA14_work/parts/lfunctions/scripts/build_items.py')
s=p.read_text().replace('−Σ_x Swan_x(V)','−Σ_x deg(x)Swan_x(V)').replace('For a finite reflexive moduleE over a Noetherian normal domain, evaluation','For a finite torsion-free moduleE over a Noetherian normal domain, evaluation').replace('Retain the ambient finiteness/reflexivity hypotheses from the printed section.','Retain the ambient finiteness and torsion-free hypotheses from the printed section; reflexivity is the asserted property of the evaluation source.').replace('polynomial ring over a PID becomes the unit ideal','polynomial ring over a UFD becomes the unit ideal')
marker='def save():\n'
insert='''# Substantive refinement following the trace/conductor re-proof.
for item in ITEMS:
    if item['id']=='SA14-462':
        item['check']='understates'
        item['check_reason']='The note correctly separates the exercises but overlooks a further global biduality defect: the printed order C need not be reflexive over A.'
        item['statement'] += ' The global identity C:B=B*:C* fails for nonreflexive C; it is valid after localization at height one, or with C=C**. The example A=Q[x,y], B=Q(sqrt(2))[x,y], C=A+(x,y)sqrt(2) has C:B=(x,y)B while B*:C*=B.'
        item['reconstruction'] += ' This additional counterexample is ours; it satisfies all finite, normal-base, separable-fraction-field hypotheses.'
for entry in ENTRIES:
    if entry['entry_id']=='MPL_60_002-035#72':
        entry['verdict']='corrected'
        entry['reason']='Retain the trace, different and local Gorenstein discussion, but replace the unqualified global biduality argument: C need not be reflexive. A=Q[x,y], B=Q(sqrt(2))[x,y], C=A+(x,y)sqrt(2) gives C:B=(x,y)B and B*:C*=B. The height-one identity remains valid.'
'''
s=s.replace(marker,insert+marker)
p.write_text(s)
p=Path('SA14_work/parts/lfunctions/scripts/build_claims.py');s=p.read_text();s=s.replace('a recurrence checkpoint is added to the calculation output','the general recurrence is checked against the primary proof in proof_notes.md')
insert='''add(562,[462],[24],'002-035','652','χ(a,C)=χ(aB,B) iff a pseudo-inversible','For an ideal of a one-dimensional order, equality of its local colength and the normalization colength is equivalent to local principality; use length, not the defective minimal-power degree.','stated without proof','E','An independent local length proof is given in proof_notes.md. Stacks02QX fixes the multiplicity convention; the statement is separated from the faulty global degree wording.','Stacks02QX','LF-S09','','Established after the stated length correction; reduction to an infinite residue field is by a faithfully flat local extension.',attribution='reused printed Bourbaki exercise')
add(563,[462],[22],'002-035','598','D:D=C iff C* pseudo-inversible','For a one-dimensional Cohen–Macaulay local order C over a DVR with trace-dual canonical module ω and D=C:ω, the multiplier ring D:D equals C if and only if ω is invertible.','stated without proof','E','Independently reproved by D:D=C:(Dω) and a nonzero socle in C/xC; no claim is made that an opened source states this exact converse. The trace-dual framework is verified in Stacks0BW0.','Stacks0BW0','LF-S09','','Complete local proof saved in proof_notes.md; regular parameter and locality are essential. The codimension-one global form follows by localization.',attribution='reused printed Bourbaki exercise')
add(564,[462],[24],'002-035','656','f=B*:C* (refined scope)','If C is reflexive over the normal base A, then C:B=B*:C*. For every full order C, this equality and f_p C*_p=B*_p hold after localization at each height-one prime of A.','stated without proof','E','This is our explicitly labelled refinement of C-SA14-467, proved using trace biduality over DVRs. Stacks0BW0 and0BM4 verify the trace and reflexive-normalization framework.','Stacks0BW0;Stacks0BM4','LF-S09','CALC-21','The global formula without C=C** is false; the corrected local formula is fully proved.',attribution='our scope refinement of a reused printed assertion')
for c in C:
    if c['id']=='C-SA14-467':
        c.update(statement='The printed global equality C:B=B*:C* is false for a nonreflexive order C, even in characteristic zero with separable fraction fields. Its height-one localization is valid; the refined statement is C-SA14-564.',status_on_pages='false as stated',**{'class':'E'},fate='Trace duality identifies B*:C* with the conductor of the reflexive hull C**, not always with C:B. The independent polynomial-ring counterexample is saved in CALC-21 and proof_notes.md.',present_status='As of 2026-11-19: refuted literally by A=Q[x,y], B=Q(sqrt(2))[x,y], C=A+(x,y)sqrt(2); the conductor is (x,y)B while both trace duals equal B. C-SA14-564 gives the precise refinement.',computation='scripts/calculations.py; outputs/calculations.txt; CALC-21; proof_notes.md',confidence='high')
    if c['id']=='C-SA14-468':
        c.update(statement='At height one, D_C=C:C* is contained in the conductor and in D_B. The equality D_C B=f D_B holds if and only if C* is invertible over C at those localizations.',fate='Independently proved using f C*=B*, the invertibility of B* over the semilocal Dedekind normalization, and lying over for the ideal D_C C*. The Gorenstein interpretation is verified in Marseglia2019 §2.',present_status='As of 2026-11-19: the local equivalence is established; global unreﬂexified products are not asserted.',confidence='high')
    if c['id']=='C-SA14-469':
        c.update(fate='Marseglia2019 §2 gives the proper-ideal and invertible-trace-dual equivalence. The distinct different-multiplier converse is independently proved in C-SA14-563.',present_status='As of 2026-11-19: both local criteria are established, with different proofs and no conflation of their quantifiers.',confidence='high')
'''
s=s.replace('def save():\n',insert+'def save():\n');p.write_text(s)
