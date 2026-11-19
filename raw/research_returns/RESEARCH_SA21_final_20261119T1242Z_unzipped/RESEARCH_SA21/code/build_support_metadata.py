"""Maintain the Part A statement/check register from explicit audited records."""
import csv
from pathlib import Path

root=Path(__file__).resolve().parents[1]
part=root/'parts/supports'
claims=[
('A01','Orthoset polarity and basis definitions','Known','','156-9/51-53'),
('A02','Support sets form a complete ortholattice, including the empty case','Known','A01','156-9/51-53,78-80'),
('A03','Exact maximal-chain/neighbourhood criterion for orthomodularity for arbitrary posets','Known','A02','156-9/109-117'),
('A04','Exact point-neighbourhood criterion for Booleanity for arbitrary orthosets','Proved','A02','156-9/109-117'),
('A05','Interval magasin data; prefigures versus incidence-closed figures','Proved','','156-8/90-127;156-9/5-7'),
('A06','Exact all-poset orthomodularity test and Boolean interval-magasin classification','Proved','A03;A04;A05;A12','156-9/5-22'),
('A07','Eight-stratum interval magasin refutes global OML and the Sumner equivalence L2','Refuted','A05;A08;A09','156-9/21-22'),
('A08','Sumner normality characterizes support calculus for all finite cliques, not OML','Proved','A16','156-8/88;156-9/117'),
('A09','Every finite prefigure of every interval magasin satisfies supp1','Proved','A05;A16','156-9/21-22'),
('A10','Infinite-figure extension of interval supp1 is false','Refuted','A05','156-9/21-23'),
('A11','Ten-element ortholattice reconstructed and nonorthomodularity verified','Proved','','156-9/113'),
('A12','Faithful magasin supports are exactly Alexandrov regular opens','Proved','A02;A04','156-8/74-89'),
('A13','MagL2/divisibility reduction to lieu graph gives exact OML class','Proved','A03;A04','156-8/15-17'),
('A14','Exact atom criterion, distinguished from singleton separation','Proved','A02;A13','156-9/3'),
('A15','Nondisjoint lieux do not exactly detect non-Booleanity; corrected faithfulness equivalence','Refuted','A04;A13;A14','156-7/82-84;156-9/3,109-117'),
('A16','Exact two-neighbourhood condition for the full figure support theorem','Proved','A02','156-7/94;156-8/88'),
('A17','Universal spatial figure axiom is OML; actual-figure axiom is strictly weaker','Proved','A07;A08;A13;A16','156-9/109-111,117'),
('A18','Explicit O6 and spatial C5 disjunctive-magma failures of supp1','Refuted','A13;A19','156-8/88-89'),
('A19','Five-cycle refutes older theorem under every stated older hypothesis','Refuted','A16','156-7/87,94'),
('A20','Faithful normalized external support need not be fully faithful','Proved','','156-8/86,88'),
('A21','Spatios are complete ortholattices; radical removal gives orthosets','Proved','A02','156-9/51-53,61,78-80'),
('A22','Final saturated correspondences are complete join maps, not ordinary orthogonality morphisms','Proved','A21','156-9/95-100'),
('A23','Spatial reconstruction with fully typed deployment target; weak reading refuted','Proved','A02','156-9/46-50'),
('A24','Supplied eight-stratum R5 counterexample rechecked, both conclusions fail','Proved','A16','156-7/94-99'),
('A25','Cograph sufficiency is strict even among Boolean comparability examples','Proved','A02','156-9/109-117')]
fields=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
with (part/'results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(fields)
 for ident,claim,status,deps,pages in claims:
  ident='SA21-'+ident
  w.writerow([ident,claim,status,'parts/supports/supports.tex label '+ident,
              ';'.join('SA21-'+x for x in deps.split(';') if x),pages,
              'Full proof in paper; finite certificate where applicable; independent audit events separately recorded.'])
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; effort not separately exposed by runtime; /root; RESEARCH_SA21 run 2026-11-19'
rows=[]
for ident,claim,status,deps,pages in claims:
 rows.append(['SA21-'+ident,'2026-11-19',who,'targeted proof check',
              'Proof and scope checked while writing; '+claim])
for ident in ['A02','A03','A04','A07','A08','A11','A13','A14','A15','A18','A19','A20','A22','A23','A24','A25']:
 rows.append(['SA21-'+ident,'2026-11-19',who,'computation or formal certificate',
              'check_supports.py passed; complete JSON in code/outputs/check_supports.json. Exhaustive graph cross-check through five vertices where relevant.'])
for ident,outcome in [
 ('SA21-R8-25','Reproved as SA21-A12; preorder and Alexandrov convention specified.'),
 ('SA21-R9-10','Reproved with exact distinct-atom hypothesis as SA21-A15; twin counterexample verified.'),
 ('SA21-R9-05','Orthomodular-law identification of scans109-111 independently rederived in SA21-A17.'),
 ('SA21-R9-06','O6 finite polarity verified; universal spatial quantifier clarified in SA21-A17.'),
 ('SA21-R9-07','MO2 verified by complete closed-set operations in check_supports.py; SA21-A15.'),
 ('SA21-R9-08','Universal spatial two-element figure axiom proved equivalent to OML as SA21-A17; actual-figure quantifier distinguished.'),
 ('SA21-K7b-15','Original eight-stratum model verified, including old absorption and both failed formulas; SA21-A24.'),
 ('SA21-R7b-21','Original eight-stratum model independently computed; 18 old full-disjunction supports; SA21-A24.'),
 ('SA21-R9b-06','Finite interval-figure support calculus independently proved in SA21-A09; infinite extension expressly refuted in SA21-A10.'),
 ('SA21-R9b-28','Finite-figure assertion rechecked by the general proof A09 and the independent all-poset census. Original 4724-figure count is not claimed to have been rerun.')]:
 rows.append([ident,'2026-11-19',who,'used and rechecked in this run',outcome])
with (part/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(rows)

