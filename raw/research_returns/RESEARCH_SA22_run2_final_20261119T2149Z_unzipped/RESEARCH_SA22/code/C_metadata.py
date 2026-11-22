#!/usr/bin/env python3
from pathlib import Path
import csv,re,json
base=Path(__file__).resolve().parents[1]
p=base/'sections/part_C.tex'
s=p.read_text()
s=s.replace('\\begin{remark}[Proved correction of the proof on scan~041]\n','\\begin{remark}[Proved correction of the proof on scan~041]\n\\label{C:proof-correction}\n')
s=s.replace('\\begin{remark}[Scope of the classification]\n','\\begin{remark}[Proved: scope of the classification]\n\\label{C:classification-scope}\n')
s=s.replace('We use differential operators in the iterated-commutator sense of EGA~IV, \\S16.8, equivalently the recursive definition in the Stacks Project, Definition~10.133.1, tag~09CH. The latter source was opened and its definition checked.', 'We use differential operators in the iterated-commutator sense of Grothendieck and Dieudonn\\\'e (1967), EGA~IV, Proposition~16.8.8 (printed pp.~42--43), equivalently the recursive definition in the Stacks Project, Definition~10.133.1, tag~09CH. Both sources were opened and the equivalence checked~\\cite{C_EGAIV4,C_Stacks09CH}.')
s=s.replace('Madiman, Wang, and Woo (2020 version; published 2021)', 'Madiman, Wang, and Woo (2020 version; published 2021)~\\cite{C_MWW2021}')
p.write_text(s)
rows=[
('explog','Finite and elementwise exponential/logarithm are inverse and natural under intertwiners','Proved','68/036-040',''),
('unipotent','Exponential/logarithm classifies globally or locally unipotent algebra automorphisms','Proved','68/040-043,045','C:explog'),
('filtered','Filtration-raising derivations exponentiate bijectively to identity-on-associated-graded automorphisms','Proved','68/045-046','C:unipotent'),
('differential','Differential order <= n is equivalent to J_U^(n+1)=0; exponential subclass is global unipotence','Proved','68/045-046','C:unipotent'),
('conormal','For J^q=0, exponential of nilpotent derivation iff conormal action uniformly unipotent; explicit exponent bound','Proved','68/045-046','C:unipotent; C:differential'),
('squarezero','Exact semidirect description of automorphisms of B plus square-zero module, with exponential criterion','Proved','68/045-046','C:differential; C:unipotent'),
('counterexamples','Differential does not imply exponential of nilpotent derivation; D(A) subset nilpotent ideal does not imply nilpotence','Refuted','68/045-046','C:filtered; C:differential; C:conormal'),
('intertwine','Time-one exponential intertwining iff operator intertwining for locally nilpotent operators on arbitrary modules','Proved','68/040-042','C:explog'),
('proof-correction','Scan041 requires Hom_K(M,N), not End_K(M); coefficients are -1/(i+j+1)!','Proved','68/041','C:intertwine'),
('module-actions','Formal additive actions correspond to all endomorphisms; ordinary actions to locally nilpotent endomorphisms','Proved','68/039','C:explog'),
('functor-criterion','Exact image/fiber and bijectivity obstruction tests for arbitrary module functors','Proved','68/043-044','C:explog'),
('functor-counterexamples','Universal formal and ordinary bijectivity for arbitrary module functors is false','Refuted','68/044','C:functor-criterion'),
('majorization','Rearrangement and weak-majorization equivalences plus exact finite convex reduction','Proved','68/019-020',''),
('pretasse-cones','The system axioms imply peak extremality of every pair in the cone-wise span','Proved','68/017,020-022','C:majorization'),
('K-counterexample','System axioms do not imply K, even with full finite nondegeneracy and exact kernel','Refuted','68/017,021','C:pretasse-cones'),
('K-repair','Generator pair extremality is exactly the additional condition needed for K under cardinality coverage','Proved under stated hypotheses','68/017,021-022','C:majorization; C:pretasse-cones'),
('group-classification','Literal axioms: all groups; with typed kernel G[2]: exactly groups with pairwise commuting involutions','Proved under stated hypotheses','68/017,022',''),
('integer-system','Centered intervals give full-cardinality systems on Z and even cyclic groups with specified index groups','Proved','68/017',''),
('classification-scope','Extra infinite coverage/nonempty-fiber/minimal-index requirements are not present in printed axioms','Proved','68/017,021','C:group-classification'),
('symmetry','Pretasse and tasse symmetry fail on S3; universal reversal by inversion and abelian symmetry hold','Refuted','68/020-021','C:majorization'),
]
with (base/'C_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes'])
 for i,(lab,statement,status,pages,deps) in enumerate(rows,1):
  notes=''
  if lab=='group-classification':notes='Literal printed quantifiers; empty fibers allowed, no cardinality coverage imposed. This is not a strengthened nondegenerate classification.'
  if lab=='K-repair':notes='Cardinality coverage holds in C4 counterexample; generator extremality fails there.'
  if lab=='module-actions':notes='Finite generation sufficient, not necessary; counterexample K=Q[x], direct sum K/(x-n).'
  w.writerow([f'C.{i:02}',statement,status,f'sections/part_C.tex, label C:{lab}',deps,pages,notes])
with (base/'C_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
 who='GPT-6 Astra (OpenAI), inherited reasoning effort, run /root/algebra_c, ChatGPT Pro mode'
 for i,(lab,statement,status,pages,deps) in enumerate(rows,1):
  w.writerow([f'C.{i:02} / C:{lab}','2026-11-19',who,'targeted proof check',f'{status}; complete argument in part_C.tex; scope {pages}'])
 for lab,program in [('counterexamples','C_finite_checks.py'),('functor-counterexamples','C_finite_checks.py'),('K-counterexample','C_full_cyclic_certificate.py'),('symmetry','C_finite_checks.py'),('group-classification','C_full_cyclic_certificate.py')]:
  w.writerow(['C:'+lab,'2026-11-19',who,'computation or formal certificate','PASS: exact rational/integer certificate; code/'+program])
 for sid,pages,note in [
 ('SA22-10','68/039','Correction confirmed and sharpened: local nilpotence is exact; finite generation is sufficient, not necessary.'),
 ('SA22-10','68/040-042','Intertwining re-proved and extended; Hom typing error on041 additionally corrected.'),
 ('SA22-10','68/045-046','Differential order criterion verified; false corollaries refuted with exact matrices; filtered and conormal repairs proved.'),
 ('SA22-10','68/044','General functor question settled by counterexamples and exact image/fiber criterion.'),
 ('SA22-2','68/019-021','Rearrangement equivalences re-proved; both asymmetries certified on S3.'),
 ('SA22-2','68/017','Lettered axioms and duplicate d lines inspected on original scan; complete C4 model verified.'),
 ('L8','68/017,021','False: complete C4 counterexample satisfies full cardinality coverage and exact prescribed kernel; replacement C:K-repair.')]:
  w.writerow([sid+' '+pages,'2026-11-19',who,'refuted, with refined statement C:K-repair' if sid=='L8' else 'used and rechecked in this run',note])
 w.writerow(['SOURCE-COTE68','2026-11-19',who,'targeted proof check','Original official images directly viewed: scans017,020,021,022,039,041,044,045,046. Transcriptions compared where used.'])
 w.writerow(['EGA-IV4-16.8.8','2026-11-19',who,'used and rechecked in this run','Local original PDF opened; text of16.8.1,16.8.2,16.8.8,16.8.9 read; commutator criterion matches theorem used.'])
 w.writerow(['MWW2021-6.2/6.8','2026-11-19',who,'carried as background without fault found','PDF and arXiv TeX source opened; prime cyclic scope verified; not used to prove all-cyclic statement.'])
print('Wrote',len(rows),'statement rows and check-event ledger.')
