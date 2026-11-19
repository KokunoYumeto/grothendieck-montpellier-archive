"""Integrate the audited finite super criterion and keep its ledgers in sync."""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[2]
main_path = ROOT / 'sections/part_c.tex'
part = ROOT / 'part_c'
main = main_path.read_text()
super_text = (part / 'c1_finite_super_criterion.tex').read_text()
weil_text = (part / 'c1_finite_weil_criterion.tex').read_text()
scope_marker = r'\begin{remark}[What the additional finite criterion settles]'
assert super_text.count(scope_marker) == 1
prefix, scope = super_text.split(scope_marker)
combined = prefix + weil_text + '\n\n' + scope_marker + scope
marker = r'\begin{theorem}[The narrow K3 ring already detects finite-dimensionality]'
if r'\label{c:finite-super-criterion}' not in main:
    assert main.count(marker) == 1
    main = main.replace(marker, combined + '\n\n' + marker)

old_scope = r'''For general mixed cohomology the analogous direct use of
$\operatorname{GL}_{a|b}$ would require exactness of its invariant
functor, which fails.  A chosen Chow parity splitting would permit
the ordinary reductive group $\operatorname{GL}_a\times
\operatorname{GL}_b$ and the even and odd dimension relations, but
its existence is an additional issue and it need not lie in the
requested tautological correspondence category.  The unrestricted
classification of all $(X,o)$ therefore remains distinct from the
specific K3 obstruction proved below.'''
new_scope = r'''For mixed cohomology the direct use of
$\operatorname{GL}_{a|b}$ would require exactness of its invariant
functor, which fails.  Theorem~\ref{c:finite-super-criterion}
replaces that step by projective lifting and an external algebraic
parity correspondence.  Corollary~\ref{c:finite-weil-criterion}
also separates finite existence over an arbitrary Weil coefficient
field from effective construction with specified coefficient data.
These finite criteria do not decide the resulting Chow vanishings.
The unrestricted classification of all $(X,o)$ therefore remains
distinct from the specific K3 obstruction proved below.'''
if old_scope in main:
    main = main.replace(old_scope, new_scope)
even_path = part / 'c1_finite_even_criterion.tex'
even_text = even_path.read_text()
if old_scope in even_text:
    even_path.write_text(even_text.replace(old_scope, new_scope))

old_intro = 'The requested lifting of all cohomological relations is exactly the injectivity of the cycle class map on this subring.'
new_intro = ('The requested lifting of rational cohomological relations is exactly the injectivity of the cycle class map on this subring. '
             'For a general Weil coefficient field, this rational statement is distinguished from injectivity after extending Chow coefficients to that field; '
             'the latter coefficient convention is addressed separately in Corollary~\\ref{c:finite-weil-criterion}.')
if old_intro in main:
    main = main.replace(old_intro, new_intro)
main_path.write_text(main)

bib_path = part / 'references.bib'
bib = bib_path.read_text()
new_bib = (part / 'c1_super_sources.bib').read_text()
added_keys = []
for entry in re.split(r'(?=@\w+\{)', new_bib):
    match = re.match(r'@\w+\{([^,]+),', entry)
    if match and not re.search(r'@\w+\{' + re.escape(match.group(1)) + ',', bib):
        bib += '\n' + entry
        added_keys.append(match.group(1))
bib_path.write_text(bib)

results_path = part / 'results.csv'
with results_path.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
new_rows = [
 ('c:super-projective-tensors', 'Rational projective-injective covers are mixed tensor summands', 'Proved',
  'PBW; Masuoka-Shibata3.6/5.4; elementary relative Frobenius pairing',
  'Ind=Coind has no twist because det(g1)=1 and dim(g1)=2ab; the parity-compatible category removes unwanted shifts.'),
 ('c:finite-super-criterion', 'Finite rational cycle criterion for mixed cohomology over C', 'Proved under C+(X)',
  'c:super-projective-tensors; Lehrer-Zhang2.1/2.3; external parity trace',
  'Actual finite iff under C+; scheme-theoretic super-orbit ideal; no exact super-invariants assertion; not a general Chow vanishing proof.'),
 ('c:finite-weil-criterion', 'Finite rational criterion without a rational form of Weil cohomology', 'Proved under C+_H(X)',
  'c:finite-super-criterion; rational kernel of the orbit coaction',
  'Finite existence for arbitrary algebraically closed base and characteristic-zero Weil field; effectiveness requires a presentation of the structure-constant Q-algebra. Rational and coefficient-extended relation conventions separated.'),
 ('c:finite-field-sign', 'Polynomial Frobenius correspondences give algebraic parity over Fbar_p', 'Proved in the stated Weil-theory scope',
  'Katz-Messing1974 Theorems1 and2(1)',
  'Etale and crystalline realizations included; the general theory must meet Katz-Messing sectionII. No Frobenius semisimplicity used.'),
 ('c:super-criterion-scope', 'Exact remaining scope and the minimal rectangle/Kimura equivalence', 'Proved scope clarification; classification unresolved',
  'c:finite-super-criterion; c:finite-weil-criterion; Del Padrone-Mazza3.2',
  'Under C+, the prescribed minimal rectangle is equivalent to Kimura finite-dimensionality. Neither C+ nor the actual vanishings are inferred for arbitrary inputs.')
]
existing_ids = {r['id'] for r in rows}
for label, statement, status, dependencies, notes in new_rows:
    if label not in existing_ids:
        rows.append(dict(zip(fields, [label, statement, status, 'sections/part_c.tex, label '+label,
                                      dependencies, '11:51-57; C.1(c)', notes])))
with results_path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fields)
    writer.writeheader()
    writer.writerows(rows)

events_path = part / 'CHECK_EVENTS.tsv'
with events_path.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    event_fields = reader.fieldnames
    events = list(reader)
event_data = [
 ('c:super-projective-tensors','/root/part_c','targeted proof check','PBW finite induction, trivial determinant and parity twists, relative top-coefficient pairing, rational integration and parity-compatible matrix coefficients checked in full.'),
 ('c:super-projective-tensors','/root/part_d','independent re-proof','Complete independent proof and written-fragment audit passed; saved in part_d/c1_superprojective_independent_audit.md.'),
 ('c:super-projective-tensors','/root','independent re-proof','Root read the entire written lemma and independent audit; rational mixed projectives and locally finite projective lifting passed.'),
 ('c:finite-super-criterion','/root/part_c','targeted proof check','Verified schematic super-orbit kernel, finite elimination, super FFT/SFT bending and polarization, projective lift and external parity-trace cancellation.'),
 ('c:finite-super-criterion','/root/part_d','independent re-proof','Full written criterion passed, including all mixed relations, Q descent, no parity idempotence assumption and normalization into the narrow ring.'),
 ('c:finite-super-criterion','/root','independent re-proof','Root read the full written criterion and D audit, accepted with C+, rational Betti and schematic orbit scope.'),
 ('c:finite-super-criterion','/root/part_c','computation or formal certificate','check_super_rectangle.py passes five superdimension rectangle cases on1490 tensor basis vectors, GL(1|1) permutation ranks6 and20, and superdimension0 versus parity trace4. Finite certificates only.'),
 ('c:finite-weil-criterion','/root/part_c','targeted proof check','I_Q is a Q-comodule kernel capturing precisely rational covariants vanishing at t; finite ideal and projective construction remain rational; effectivity requires coefficient-algebra equations.'),
 ('c:finite-weil-criterion','/root/part_d','independent re-proof','Independently checked the arbitrary-Weil-field kernel construction, exact rational-relation scope and absence of a required rational cup-algebra form.'),
 ('c:finite-weil-criterion','/root','independent re-proof','Root proposed and independently checked the I_Q comodule-kernel extension and finite-existence/effectiveness distinction.'),
 ('c:finite-field-sign','/root/part_c','targeted proof check','Opened and OCR-read original Katz-Messing pp73-77, including full Theorem1 proof and Theorem2(1) polynomial-projector proof; explicit cohomology hypotheses retained.'),
 ('c:super-criterion-scope','/root/part_c','targeted proof check','Read Del Padrone-Mazza complete Theorem2.1 and Proposition3.1/Theorem3.2 proofs; minimal rectangle under C+ implies and is implied by Kimura finiteness, with no general Schur-finiteness substitution.'),
 ('c:super-criterion-scope','/root/part_d','independent re-proof','D independently located and checked original Theorem3.2 p286 and the exact rectangle hypothesis; unrestricted classification remains open.'),
 ('c:finite-criterion-scope','/root/part_c','scope correction','Updated earlier mixed-parity caveat to refer to the proved projective/C+ criterion and arbitrary-Weil-field finite-existence extension; no general Chow classification claimed.')
]
event_keys = {(e['statement_id'],e['who'],e['outcome']) for e in events}
for label, who, kind, outcome in event_data:
    who = 'GPT-6 Astra (OpenAI), '+who
    if (label,who,outcome) not in event_keys:
        events.append(dict(zip(event_fields,[label,'2026-11-19',who,kind,outcome])))
with events_path.open('w',newline='') as f:
    writer=csv.DictWriter(f,event_fields,delimiter='\t')
    writer.writeheader(); writer.writerows(events)

sources_path = part / 'sources.tsv'
with sources_path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t'); source_fields=reader.fieldnames; sources=list(reader)
source_data=[
 ('c_lehrerzhang2021super','https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/second-fundamental-theorem-of-invariant-theory-for-the-orthosymplectic-supergroup/C0A3AB442E2DAB0D9F7EECD88DF8AE3E','Theorems2.1/2.3;Corollaries2.2/2.5;AppendixA.1/A.2;all relevant proof text'),
 ('c_heidersdorf2017mixed','https://arxiv.org/pdf/1406.0444','Version3;Theorem1.1p2;categoryR pp3-4;Theorem3.2p6'),
 ('c_masuokashibata2017super','https://arxiv.org/pdf/1304.0531','Version8;Cor3.6p9;hy=U p22;Prop5.4withproofpp23-24;Thm5.8/Cor5.10p26'),
 ('c_tabuada2018sign','https://research.unl.pt/ws/portalfiles/portal/82273576/S0002-9939-2018-13955-6.pdf','Section1p1389:definition of C+ only'),
 ('c_delpadronemazza2005','https://www.numdam.org/item/10.1016/j.crma.2005.07.010.pdf','CompleteThm2.1pp284-285;Prop3.1/Thm3.2p286'),
 ('c_katzmessing1974','https://web.math.princeton.edu/~nmk/old/katzmessing.pdf','Originalscan+OCR completepp73-77;IIhypotheses;Thm1pp74-75;Thm2(1)pp76-77')
]
source_ids={s['key'] for s in sources}
for key,url,locators in source_data:
    if key not in source_ids:
        sources.append(dict(zip(source_fields,[key,'opened primary full text and relevant proofs',url,locators])))
with sources_path.open('w',newline='') as f:
    writer=csv.DictWriter(f,source_fields,delimiter='\t'); writer.writeheader(); writer.writerows(sources)

notes_path=part/'part_c_notes.md'
note_heading='## Finite mixed-parity criterion and arbitrary Weil fields (05:30 UTC)'
notes=notes_path.read_text()
if note_heading not in notes:
    new_notes='''

## Finite mixed-parity criterion and arbitrary Weil fields (05:30 UTC)

The full superprojective proof is integrated and independently audited by D and root. Under C+ it gives a finite iff for the all-powers narrow Chow relations. Its inputs are the Euler/point normalizations, the minimal rectangular Schur relation, and finitely many orbit-ideal covariant cycles. The super-orbit ideal is schematic, retaining odd nilpotents. Finite projective-injective rational modules replace the invalid exact-invariants step; an external algebraic parity correspondence gives a positive trace and cancels the projective factor. It need not be a Chow idempotent or a narrow correspondence.

The rational-kernel extension removes the need for a rational form of cohomology: for a K-valued cup table use ker(R_Q -> O(G_Q) tensor K). It is Q-stable and captures exactly rational relations. Finite existence holds over any algebraically closed base under the sign hypothesis; an effective algorithm additionally needs a presentation of the Q-algebra of structure constants. Relations with K coefficients in Chow tensor K are explicitly separated. Over Fbar_p the sign hypothesis is supplied by Katz-Messing polynomial Frobenius projectors for etale/crystalline cohomology and their stated class of Weil theories.

Del Padrone-Mazza Theorem3.2, fully opened, shows that under C+ the exact minimal rectangle is equivalent to Kimura finite-dimensionality. Thus finite criteria do not remove the actual Chow vanishing problem, nor settle the general K3 determinant. Arbitrary-pair classification remains unresolved. Five small super-rectangle checks and exact permutation ranks are archived as finite certificates, not substitutes for the general invariant theory.

Further routes considered: ordinary super-invariants are not exact; a finite free resolution is not automatic for an exterior algebra (the trivial module over Lambda(epsilon) has an infinite periodic resolution). General associative Specht finite-basis theorems do not immediately give relations for a traced commutative Frobenius algebra PROP. No reduction identifying those tensor ideals was proved. Root's proposed propagation of the new R0 weight bound to interior degrees is ruled out by the already proved Legendre Sym^j R1 example, which attains the old upper weight.
'''
    notes=notes.replace('# Part C research ledger','# Part C research ledger'+new_notes,1)
    notes_path.write_text(notes)

print(json.dumps({'main_lines':len(main.splitlines()),'new_labels':[x[0] for x in new_rows],
                  'bib_keys_added':added_keys,'result_rows':len(rows),'check_events':len(events)},indent=2))
