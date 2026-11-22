#!/usr/bin/env python3
"""Integrate independently checked additions for the fifth scheduled snapshot."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
p=root/'sections/A_functorial_skeleton.tex'
p.write_text(p.read_text().replace('a,quad y','a,\\quad y'))
p=root/'RESEARCH_SA08_C3_D031_paper.tex'; s=p.read_text()
s=s.replace('\\input{sections/A_paths}\n','\\input{sections/A_paths}\n\\input{sections/A_skeleton_replacement}\n\\input{sections/A_functorial_skeleton}\n')
s=s.replace('\\input{sections/A_resolved_tail_repair}\n','\\input{sections/A_resolved_tail_repair}\n\\input{sections/A_relative_resolved_tail}\n\\input{sections/A_iterated_saturation}\n\\input{sections/B_resolved_tail_lattice}\n\\input{sections/B_saturated_degree_two}\n\\input{sections/A_saturated_tail_H3}\n\\input{sections/A_resolved_tail_period}\n\\input{sections/A_second_skeleton_obstruction}\n')
p.write_text(s)
p=root/'notes/A_root_results.csv'
with p.open(newline='') as f: reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
for r in rows:
 if r['id']=='A-CS':
  r['depends_on']='A-001–006; AT17–18; A-SAT01; A-L11–12; A-S09-22–23'
  r['notes']='A-006 proves equivalence with common sources internal to the proper full subcategory C having the explicit free first skeleton P(E). The assertion for C remains undecided.'
 if r['id']=='A-TL':
  r['depends_on']='A-001–006; AT17–18; A-SAT01; A-L11–12; A-S09-22–23'
  r['notes']='A-006 gives actual functors and natural transformations inducing an equivalence with the all-arrow localization of the proper full subcategory C. Terminality there remains undecided.'
rows.extend([
 dict(zip(fields,['A-004','Every admissible theory has an actual admissible replacement with a prescribed common free first skeleton','Proved','sections/A_skeleton_replacement.tex A-004','A-001; Stacks 14.19 coskeleton','cote136 scans117–121','Explicit graph matching pullback and uniform bounds; support and flatness preserved.'])),
 dict(zip(fields,['A-005','The common-source question reduces to pairs with the same specified first skeleton P(N)','Proved','sections/A_skeleton_replacement.tex A-005','A-004','cote136 scans117–121','Both comparison arrows constructed; the restricted class is proper by a split admissible example.'])),
 dict(zip(fields,['A-006','Functorial first-skeleton replacement gives equivalent all-arrow localizations and equivalent common-source questions in a proper full subcategory','Proved','sections/A_functorial_skeleton.tex A-006','A-004–005','cote136 scans117–121','Actual functor R indexes all fillers; natural transformations jR to Id and Rj to Id. Both main gates strictly reduced; neither assertion settled.']))
])
with p.open('w',newline='') as f: w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
p=root/'notes/A_root_CHECK_EVENTS.tsv'
with p.open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for ident,detail in [
 ('A-004','Full proof checked: one-truncated identity disks, coskeleton normalization and graph sequences, actual pullback maps, uniform thresholds and optional support/flatness.'),
 ('A-005','Full proof checked: actual first-skeleton identifications and composites prove both directions; explicit split admissible object proves proper restriction.'),
 ('A-006','Full proof checked: all-filler indexing is strictly functorial; pullback R and two natural transformations give localization and nerve equivalences and internal common-source equivalence.'),
 ('AT17','Full proof read: edge contraction prescribes the boundary, target error factors through K2, Ext2 supplies actual relative lift, rational translation and quotient retain the stated properties.'),
 ('A-L11','Full proof read: complete coefficient lattices include e4; the unique rational primitive is outside the integral arity-two lattice. Twisted actual source maps to the detecting algebra.'),
 ('A-L12','Full proof read: entire degree-one lattice is Cx, d(Cx)=2xi, arity/weight argument proves persistence through every saturation stage and actual comparison kills xi.'),
 ('A-S09-22','Full proof read: complete degree-two lattice and mod2 EK detector prove order-two H3; integral J gives the corrected twisted cycle and its persistence through saturation.'),
 ('AT18','Full proof read: exact q3 residue, displayed modulo2 homotopy identity, and separately stated weight-s comparison prove the specified choice-independence.'),
 ('A-S09-23','Full proof checked: explicit normalization preimages give the free two-skeleton cover; row-one H1 comparison is an isomorphism; cellular completion gives a surjection onto the rechecked AS12 high-prime class.')]:
  w.writerow([ident,'2026-11-19','GPT-6 Astra; root; RESEARCH_SA08_C3_D031','targeted proof check',detail])
p=root/'sections/A_unresolved.tex';s=p.read_text()
old='The strongest proved comparison in this run is A-003:\nevery finite zigzag of actual admissible morphisms can be refined\nto an actual common source.  The remaining connectivity question\nis therefore precisely the existence of a finite zigzag between\narbitrary objects.  No such zigzag has been produced in general.'
new=r'''The strongest proved reduction is now A-006.  Let $\mathcal C$
be the proper full subcategory defined there by the first-skeleton
property $P(E)$.  The actual functor $R:\mathcal A\to\mathcal C$
and natural comparison $jR\Rightarrow\mathrm{Id}$ prove that
common sources for arbitrary admissible objects are equivalent
to common sources internal to $\mathcal C$ for every pair of
its objects.  This assertion for $\mathcal C$ is undecided.
A-003 additionally identifies it with connectivity by finite
zigzags.  No such zigzag between arbitrary objects of
$\mathcal C$ has been constructed.  This is a genuine restriction
of both the objects and the allowed source, with every comparison
map and both directions proved in A-006.'''
assert old in s;s=s.replace(old,new)
old='The active unresolved comparison is between that algebra and\na coefficient-resolution attachment that supplies target maps.\nNeither a low-cohomology comparison between those algebras nor\na completed admissible source is inferred.'
new=r'''AT16--17 construct the coefficient-resolution attachments with
actual target maps, including the prescribed edge boundary.
A-SAT01 supplies the iterated degree-one saturation and extends
all specified torsion-free target maps.  The direct comparison
with the two-term tail has now been refuted as a low-cohomology
equivalence: A-L11 gives an order-two degree-one class, and A-L12
and A-S09-22 give order-two classes in degrees two and three that
survive every based saturation stage.  AT18 gives the exact
coefficient residue for attaching the next degree-three repair,
and proves its stated invariance with the extra low-weight
period hypothesis explicitly retained.  A general simultaneous
vanishing or compatible repair of these residues is unproved.
A-S09-23 also refutes a second-skeleton extension using only
one-forms generated by zero-forms and their differentials, for
$N\geq2$.  The free first-skeleton reduction itself is unaffected.
No completed admissible common source follows from these steps.'''
assert old in s;s=s.replace(old,new)
s=s.replace('Let $\\mathcal A$ denote this category and invert all its morphisms.\nWe have not proved',r'''Let $\mathcal A$ denote this category and invert all its morphisms.
A-006 supplies explicit mutually inverse equivalences between
this groupoid and $\mathcal C[\operatorname{Mor}(\mathcal C)^{-1}]$.
Thus the present exact gate is terminality of the latter groupoid,
for the same proper full subcategory as above.
We have not proved''')
p.write_text(s)
p=root/'RESEARCH_SA08_C3_D031_report.md';s=p.read_text().replace('State at checkpoint 04','State at checkpoint 05')
s=s.replace('A-002–003 refine cospans and finite zigzags. Construct a zigzag between arbitrary objects, or a localization invariant separating two objects.','A-006 reduces this exactly to common sources internal to the proper full subcategory C with free first skeleton P(E). That restricted assertion remains undecided.')
s=s.replace('Common-source existence and contraction of arbitrary zigzag loops both remain to be proved.','A-006 proves an equivalence with the all-arrow localization of the proper full subcategory C. Terminality of that groupoid remains undecided.')
s=s.replace('Its nonlinear low integral cohomology remains uncomputed.','A-L11–12 and A-S09-22 now detect integral classes in degrees1,2,3; degrees2,3 survive full based saturation.')
marker='| B: exact v4 statement and conventions |'
insert='''| A: functorial first-skeleton reduction | Proved | A-004–006 construct actual admissible replacements, the functor R and natural transformations. Both main questions reduce exactly to a proper full subcategory. |
| A: relative resolved-tail attachment | Proved | AT17 supplies the actual edge boundary, target maps and rational comparison while retaining simplices0 and1. |
| A: iterated based saturation | Proved | A-SAT01 kills all torsion H1 in the stated range, extends every specified torsion-free target map and fixes simplex1 when it is integrally exact. |
| A: resolved comparison is a low-degree cohomology equivalence | Refuted | A-L11 gives an order-two H1 class; A-L12 and A-S09-22 give order-two H2 and H3 classes that survive full saturation. |
| A: precise next degree-three obstruction | Proved | AT18 identifies the coefficient residue and proves its invariance under the stated extra weight-s comparison. Its vanishing for general target maps remains open. |
| A: free zero-form second skeleton | Refuted in the stated range | A-S09-23 constructs the actual free cover and H1 comparison, proving the high-prime obstruction for every N≥2. |
'''
assert marker in s;s=s.replace(marker,insert+marker)
s=s.replace('These proofs preserve the support condition and integral termwise flatness. They have had an independent second proof check. They do not supply the first zigzag between arbitrary theories.','These proofs preserve the support condition and integral termwise flatness. They have had an independent second proof check. A-004–006 now give a further actual reduction: every object maps from a functorial replacement with free first skeleton P(E). The inclusion j of this proper full subcategory C and replacement R have natural transformations jR→Id and Rj→Id, hence induce equivalent all-arrow localizations and homotopy-equivalent nerves. Actual composition proves the equivalence of the two common-source assertions, including the requirement that the new source lie in C. These results strictly reduce both main gates. The questions for C remain unresolved.')
s=s.replace('The active comparison with a finite coefficient-resolution repair still requires control of nonlinear low cohomology.','The comparison with the finite coefficient-resolution repair is now explicit, and its nonlinear low-cohomology defects have been computed.')
s=s.replace('Its nonlinear integral low cohomology remains uncomputed.','AT17 extends the construction to the prescribed edge boundary. A-SAT01 gives the full iterated based saturation while preserving that boundary and all specified target maps. A-L11–12 and A-S09-22 compute explicit order-two classes, including H2 and H3 classes surviving all saturation stages. The strict comparison to the two-term tail kills these classes, so it is not a low-degree cohomology equivalence. AT18 identifies the next repair residue exactly and retains the extra low-weight hypothesis needed for independence of all lift choices. A-S09-23 separately obstructs the purely differential-generated second-skeleton route using an actual cellular cover and the rechecked cotangent theorem.')
rows='''| B_resolved_tail_lattice_certificate.py | 4,421 exact lattice, coefficient-resolution and primitive checks; complete weight-four generator set retained | 0.4488264289975632 |
| B_saturated_degree_two_certificate.py | 255 exact checks; complete arity-two lattices and boundary matrices in the detecting weight | 0.13798703700012993 |
| A_cosimplicial_saturated_H3_certificate.py | 30 generator d-squared checks, full degree-two detector, integral J identities, twisted cycle and parameter matrices | 0.014463970001088455 |
| A_integral_period_check.py | 22 exact symbolic checks of the modulo-two homotopy variation identity and generator differentials | 0.0009436880063731223 |
'''
s=s.replace('| B_source_audit.py |',rows+'| B_source_audit.py |')
s=s.replace('Neither main PartA gate has decreased.','At that review neither main PartA gate had decreased. Since then A-006 has reduced both gates to the proper full subcategory C by explicit functors and natural transformations; this movement will be assessed at the next scheduled review.')
p.write_text(s)
p=root/'PROGRESS_LEDGER.md'
with p.open('a') as f:f.write('''
## Working update — 19 November 2026, 19:22 Europe/Berlin

This is a dated working update, not the second formal review.

| Row | Current status | Strongest proved gate |
|---|---|---|
| A-CS | Undecided | A-006: equivalent to common sources internal to the proper full subcategory C whose first skeleton is P(E). Actual replacement R and natural comparison transfer both directions, with support and flatness retained. |
| A-TL | Undecided | A-006: equivalent to terminality of C with every morphism inverted. The inclusion and R induce inverse equivalences by two displayed natural transformations. |
| A-SA09 | Undecided application | Reconstruction statements remain verified. A-S09-23 gives the actual cotangent comparison blocking the purely zero-form-generated second skeleton for N≥2; no full comparison or separator follows. |
| B-D031 | Completed | D-031 and B-001–008 retain the independently proved counterexample, source/dependency audit and exact corrected lifting criteria. |

A-004–006 have each passed all three independent agent checks as well as the root check. The subcategory C is strictly smaller: an explicitly split admissible theory with a nonzero simplex-zero one-form does not belong to C. The equivalences and actual arrows show that this is a reduction of each main question, rather than a side calculation. Both restricted assertions remain open. The next formal review remains due18:43:12UTC /19:43:12Europe/Berlin.

Other checked additions: AT17 supplies the relative resolved tail; A-SAT01 iterates based H1 saturation; A-L11–12 and A-S09-22 detect actual integral H1/H2/H3 defects, with H2/H3 surviving saturation; AT18 identifies the next period residue with the exact scope of invariance. These additions do not themselves finish either main question.
''')
print('Integrated checkpoint05 proof and record additions.')
