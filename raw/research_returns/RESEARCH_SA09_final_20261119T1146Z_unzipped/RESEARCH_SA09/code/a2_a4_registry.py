#!/usr/bin/env python3
"""Generate the A2/A4 statement and check-event fragments."""
from pathlib import Path
import csv

root=Path(__file__).resolve().parents[1]
rows=[
 ('A2.1','The nonnegative walking-complex category is not Frobenius over a nonzero ring; stalk R[0] is projective but not injective.','Refuted','A2.6','137:49,52','Refutes the Frobenius identification in Lead L3; finite F_2 certificate.'),
 ('A2.2','For every commutative ring, relative left-exact functors out of bounded nonnegative finite-free complexes are fully faithfully determined by their disk values; the essential image is the explicit finite-matrix kernel condition.','Proved','','137:49-56','Ordinary categorical kernels; no regularity, field, or domain assumption.'),
 ('A2.3','Over a PID the essential image is characterized by cycle kernels and two-term torsion-block kernels; cycle kernels alone are insufficient for nonfields.','Proved','A2.2','137:51','Z/4 target counterexample; distinguishes PID from principal ideal rings with zero divisors.'),
 ('A2.4','For every commutative ring and Quillen exact target, exact functors correspond to admissible resolutions; strong relative-left-exactness has the stated additional admissible-kernel criterion.','Proved under stated hypotheses','A2.2;A2.3;BuehlerExact','137:49-56','Quillen axioms hold in the theorem, not in the incomplete printed Sex1-2 list; shorter strong criterion requires weak idempotent completeness.'),
 ('A2.5','The printed Sex1-2 axioms alone do not imply the essential-image characterization by resolutions.','Refuted','A2.2;A2.4','137:49-51','Finite counterexample in finite abelian groups, using pullback of Z/16 to Z/4 along multiplication by2.'),
 ('A2.6','The category of bounded finite-free complexes in all integer degrees is Frobenius; its stable category is K^b(free).','Proved','A2.1;BuehlerExact','137:49-56','Corrected two-sided Frobenius statement; does not identify this enlargement with the manuscript nonnegative category.'),
 ('A4.1','Dold-Puppe decomposition L_n=direct_sum_i N_i(L)^(binomial(n,i)); termwise finite/projective equivalences.','Known','DoldPuppe1961','137:14','Equation3.3, Theorem3.6, Corollary3.8 opened; count of surjections derived.'),
 ('A4.2','For any commutative ring and finite simplicial terms, normalization is bounded in degreeD iff all residue-field rank functions are eventually polynomial of uniformly bounded degreeD.','Proved','A4.1','137:14-15','Maximal ideals suffice; eventual equality upgrades to equality at every nonnegative n.'),
 ('A4.3','Over every regular noetherian ring, partial-perfection is equivalent to finite bounded homology; the uniform raw-rank criterion implies perfection but characterizes actual boundedness.','Known','A4.1;A4.2;Stacks066Z','137:14-15','No finite Krull dimension assumption; cited theorem opened and hypotheses translated.'),
 ('A4.4','Proposition1(e) is false in both directions even over Z; uniform degrees fix sufficiency but not necessity for derived perfection.','Refuted','A4.1;A4.2;A4.3','137:14-15','Distinct-prime unbounded homology and locally finite contractible disk complex.'),
 ('A4.5','Over a noetherian ring, pseudo-coherent normalization is perfect exactly when derived residue-field homology has a uniform bound; bounded raw normalization need not be perfect on a nonregular ring.','Known','Stacks0G99;A4.2','137:15','Complete finite characteristic-two dual-number counterexample and all-degree periodic Tor calculation.'),
 ('A4.6','Under noetherianness the binomial fiber coefficients are constructible; PID rank N_i includes mu_i+mu_i+1+beta_i+beta_i+1+nu_i; derived perfection permits infinitely many contractible disk factors.','Proved','A2.3;A4.1;A4.3','137:15,17','Both terms mu_i and mu_i+1 are necessary; strict versus derived finite-support criteria distinguished; disk certificate included.'),
]
with (root/'notes/A2_A4_results.csv').open('w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes'])
    for ident,stmt,status,deps,pages,notes in rows:
        w.writerow([ident,stmt,status,'sections/'+ident.split('.')[0]+'.tex: '+ident,deps,pages,notes])
who='GPT-6 Astra (OpenAI), inherited effort, run /root/a2_a4'
events=[]
for ident,stmt,status,deps,pages,notes in rows:
    if status=='Known':
        typ='used and rechecked in this run'
        outcome='Opened exact cited theorem and checked the derivation to the stated form; '+notes
    elif status=='Refuted':
        typ='refuted, with the refined statement\'s id'
        outcome='Complete counterexample; refinement '+deps+'; '+notes
    else:
        typ='targeted proof check'
        outcome='Complete proof written and checked against definitions; '+notes
    events.append([ident,'2026-11-19',who,typ,outcome,pages])
for ident in ['A2.1','A2.3','A2.5','A4.4','A4.5','A4.6']:
    events.append([ident,'2026-11-19',who,'computation or formal certificate',
      'code/a2_a4_checks.py; logs/a2_a4_checks.json. Scope and exact exhaustive counts in notes/A2_A4_source_log.md; all assertions passed.',''])
events += [
 ['A3.1','2026-11-19',who,'targeted proof check','Dold-Puppe equation3.3 and Theorem3.6 yield binomial ranks; Vandermonde identity, finite-free summands, polynomial tensor/Gamma ranks and extra-degeneracy identities checked. Normalized contraction obtained as projection times unnormalized contraction times inclusion.','137:38-39,46-47'],
 ['A3.2','2026-11-19',who,'targeted proof check','Checked right-adjoint evaluation variance, cosimplicial maps, reconstruction of pointwise product from full tensor pairings, finite-free tensor/function isomorphism and equalizer. Divided-power law defined by Gamma^p of each evaluation; no infinite-Hom base-change isomorphism assumed.','137:38-39,65-72,75-86'],
 ['A1.6','2026-11-19',who,'targeted proof check','Reviewed scalar-twist countermodel against scans75-84. Contradiction m(e0,e0)=e0 versus -e0 is valid for an equivalence preserving the supplied exponential comparisons and unit constraints. The gauge t_n is not exponential-monoidal because t_2 differs from t_1 squared. This check does not assert failure of an equivalence after discarding those structures.','137:75-84'],
 ['A1.7','2026-11-19',who,'targeted proof check','Checked types and finite index bounds in D_{d,m}, co-Kleisli composition, filtered Hom/direct-sum identification, weighted degree rules and strict disjoint-variable representing components. Counits should be explicitly eps_{B_m}D_{1,m}=id and B_d(eps)D_{d,1}=id, with no degree-one projection from B_0.','137:75-84'],
 ['A1.8','2026-11-19',who,'targeted proof check','Reviewed inflated graded F2 model E*(X)=D*(X) tensor D*(TX) with second factor in external weight3. Retract formulas satisfy homogeneous associativity by naturality and pi i=id; unit cases reduce to E^n(1)=1. The obstruction rules out coherent natural cubic enrichment, not separately chosen basis-dependent Hom laws. Natural addition forces (x+y)^3=x^3+y^3, contradicted in F4 by x=1,y=omega.','137:82-86'],
 ['L3','2026-11-19',who,'refuted, with the refined statement\'s id','A2.1 refutes Frobenius status of the manuscript nonnegative source; A2.2-A2.4 establish the correct universal property; A2.6 gives the valid two-sided Frobenius enlargement.','137:49-56'],
 ['SA09-3','2026-11-19',who,'refuted, with the refined statement\'s id','Study reading lines195-198 and previous CHECK_EVENTS line18 conflate nonnegative and two-sided categories; corrected by A2.1,A2.2,A2.6. Full faithfulness survives.','137:49-56'],
 ['SA09-3','2026-11-19',who,'independent re-proof','Recomputed all relevant kernel conditions from the explicit disk copresentation; PID torsion kernels in R3 are correct; all-ring extension A2.2.','137:51-56'],
 ['SA09-3','2026-11-19',who,'used and rechecked in this run','Walking complex disk Hom groups and degree signs checked directly; normalized nonnegative indexing retained.','137:40-41,49-56'],
 ['SA09-2','2026-11-19',who,'independent re-proof','Uniform fiber-rank criterion proved by nonnegative binomial coefficients and Nakayama over every commutative ring with finite terms, A4.2; original e both directions refuted by A4.4.','137:14-15'],
 ['SA09-2','2026-11-19',who,'targeted proof check','PID block decomposition gives rank N_i=mu_i+mu_i+1+beta_i+beta_i+1+nu_i, A4.6; independent mathematical check, not an ink inspection.','137:17'],
]
with (root/'notes/A2_A4_CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    w.writerow(['statement_id','date','who','type','outcome','manuscript_pages'])
    w.writerows(events)
print('Wrote',len(rows),'statement rows and',len(events),'check events.')
