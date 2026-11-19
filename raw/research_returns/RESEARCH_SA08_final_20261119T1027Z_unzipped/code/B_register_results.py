from pathlib import Path
import csv,json
base=Path(__file__).resolve().parents[1]
rows=[
('B-01','Corrected three-data classification for arbitrary PD triples','Proved','B.1, proof of B-01','PD polynomial/exterior presentation','136:162-164,184-188','Includes M and 2B_iL=0; t=0 allowed.'),
('B-02','Missing M, unrestricted PD preservation, and 2-invertible margins are false','Refuted; exact replacements proved','B.1, B-02','B-01','136:162,166,170,172,186','F2 and F3 witnesses; arbitrary scalar PD ideal scope correction.'),
('B-03','Continuous completed automorphisms, group law, determinant converse','Proved under stated hypotheses','B.1 continued, B-03','B-01','136:174-178','Total-weight continuity is explicit; abstract discontinuous automorphisms not covered.'),
('B-04','Omega_cont=E semidirect P; row-finite ind-affine parameter functor, non-affine','Proved under stated hypotheses','B.1 continued, B-04','B-03','136:178-180','Free B data indexed by powers of2; product-of-rings obstruction to affineness.'),
('B-05','Fixed-weight cycle modules are linearly homotopy equivalent to K(k,i)','Proved','B.2, B-05','Integral PD Poincare contraction; Dold-Kan','136:8-10,222-239','Normalized modules projective; positive-degree linear maps nullhomotopic.'),
('B-06','Full complete cohomology action is coefficient substitution; positive-degree components vanish','Proved under stated hypotheses','B.2, B-06','B-03;B-05;A weightwise comparison','136:180-182','Every ring and simplicial set; total-weight continuous maps; phi0-semilinearity retained.'),
('B-07','Literal determinant-only action L4 is false','Refuted; exact replacement B-06','B.2, B-07','B-03;B-06','136:180','Point over Z; A=X+X^(2), Delta1, nontrivial T substitution.'),
('B-08','B-automorphisms induce identity and no positive Steenrod square','Proved under stated hypotheses','B.3, B-08','B-06','136:182','Continuous completed B maps; all k, in particular F2.'),
('B-09','RP3 sphere test cannot determine positive-degree cohomology operations','Refuted; replacement universal K(k,i) test','B.3, B-09','Steenrod-Epstein I.1 axiom3;finite certificate','136:182','32,768 one-cochains checked on six-vertex RP2 triangulation.'),
('B-10','Strict natural tau_omega automorphisms yield only identity on ordinary F2-cohomology','Proved under stated hypotheses','B.3, B-10','Exact shadow reconstruction from Part A.2;B-05','136:182,244-281','Either honest Serre quotient specified; does not assert classification of derived-only transformations.'),
('B-11','Exact range of Omega operations; exclusive Ga-versus-Steenrod placement L8 false','Refuted; exact replacement proved','B.5, B-11','B-06;B-08;B-10;Breen4.1,4.6','136:182,374','Identity lies in both; P0=F differs from unit; lowest-weight lambda^i not stable if lambda!=1.'),
('B-12','Rescaling monoid units and square-zero torsion intersection','Proved','B.4, B-12','Divided-power multiplication;Legendre formula','136:204-208','All rings; finite-polynomial and completed cases distinguished; 262144 integer pairs checked.'),
('B-13','Semidirect monoid diagrams false; corrected split automorphism extension','Refuted; exact replacement proved','B.4, B-13','B-01;B-12','136:206-208','Q counterexample A=X(T-X), scalar T0; full PD substitution group supplies section.'),
]
with (base/'notes'/'B_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes']);w.writerows(rows)
with (base/'notes'/'B_CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
    for r in rows:
        ty='refuted, with the refined statement\'s id' if r[2].startswith('Refuted') else 'independent re-proof'
        w.writerow([r[0],'2026-11-19','GPT-6 Astra (OpenAI), automorphisms parallel run',ty,r[2]+'; '+r[3]+'; '+r[6]])
    for old,new,out in [
        ('CE-A12','B-01/B-02','Missing M independently re-derived; complete corrected classification written.'),
        ('CO-A03','B-01/B-02','F2 relation witness independently checked.'),
        ('CE-B02','B-01','Two-variable coefficient commutators verified.'),
        ('CO-B01','B-02','Omitted-M defect confirmed.'),
        ('CE-A15','B-02','F3 margin counterexample verified; reduced refers to k, not divided-power S.'),
        ('CE-A21','B-03/B-04','Continuous completion parameters and determinant inverse proved.'),
        ('CE-A22','B-04','Binary-generator and row-finiteness description proved; non-affine proof added.'),
        ('S3-136-002-141-CE001','B-05','Integral Poincare contraction and fixed-weight cycle homotopy re-derived.'),
        ('S3-136-002-141-CE004','B-06','Weightwise scalar action re-derived through exact resolutions.'),
        ('L4','B-07','False literally on a point; corrected phi0-semilinear action B-06.'),
        ('L8','B-11','Exclusive operation-algebra placement refuted; actual range specified.'),
    ]:w.writerow([old,'2026-11-19','GPT-6 Astra (OpenAI), automorphisms parallel run','used and rechecked in this run',out+' See '+new+'.'])
    w.writerow(['B-computation','2026-11-19','GPT-6 Astra (OpenAI), automorphisms parallel run','computation or formal certificate','B_finite_checks.py; 262144 binomial pairs,32768 RP2 cochains,169 matrix identities; exact run1.808541720998619 seconds.'])
print('Wrote',len(rows),'statement rows and complete check-event table.')
