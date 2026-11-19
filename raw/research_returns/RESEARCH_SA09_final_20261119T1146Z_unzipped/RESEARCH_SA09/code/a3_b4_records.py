"""Write the A3/B4 statement register and actual check events."""
from pathlib import Path
import csv,json
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
rows=[
('A3.1','Right-adjoint cochain tests R_n are bounded finite free split acyclic and denormalize the walking complex; test category closed under tensor and divided powers','Proved','sections/A3.tex:A3.1','DoldPuppe1961 §3 (3.3), Thm3.6, (3.20);A2.2','137:37-39,47','Integral coefficients; finite ranks and normalized contraction explicit; Yoneda identifies full cosimplicial test object'),
('A3.2','Normalized cochains with the full natural Gamma action on the test functor determine and are determined by its tensor/unit/Gamma structure and the cosimplicial function ring Z^X','Proved','sections/A3.tex:A3.2','A3.1;A2.2','137:38-39','rho_2 cross effect recovers tensor pairing; rho_0 recovers unit; all hypotheses constructed for actual F_X; on the image of spaces'),
('A3.3','Full Gamma data recover nilpotent finite-type homotopy types; binomial derived maps recover connected mapping spaces; E-infinity and ordinary affine realizations have extra maps/points','Known, with comparison proved','sections/A3.tex:A3.3','A3.2;Horel2025 Thm5.4;Mandell2006 Main Thm,Thms0.1-0.2;Mandell2002 Thms5.5,5.8;Toen2020 Thm4.1,Cor5.1,5.4,5.5','137:39','Toën only simply connected; finite disconnected case follows by primitive idempotents; rational comparison requires Q contained in k'),
('A3.4','Bare integral cochain quasi-isomorphism type with graded H-cup and degree-compatible positive divided powers determines nilpotent finite CW homotopy type','Refuted','sections/A3.tex:A3.4','CFH2016 Prop1.2;code/a3_b4_verify.py','137:39,72','Counterexample L(5,1),L(5,2); not a refutation of coherent chain multiplication or A3.2'),
('A3.5','Binomial numerical operations are strict polynomial laws; the unital ring Z admits PD operations on an ideal containing 1','Refuted','sections/A3.tex:A3.5','code/a3_b4_verify.py','137:38,75-86','Inputs 0 and 2 agree mod 2 but binomial outputs differ; 2 gamma_2(1)=1 impossible'),
('B4.1','Exact Kummer image of 2 and 1/2 is parity kernel (-1)^b=chi_2(a); level index 2 iff 8 divides N','Proved','sections/B4.tex:B4.1','','138:19,36,40','Eisenstein and real abelian subfield proof excludes all other entanglements; N=1,2,4,8 included'),
('B4.2','Exact Kummer image of -1/2 is parity kernel (-1)^c=chi_minus2(a), c=(a-1)/2-b; same level indices','Proved','sections/B4.tex:B4.2','B4.1','138:35-41','Finite translation requires cyclotomic lift modulo 2N; full formula well-defined adelically'),
('B4.3','All E(alpha-prime(i)) fibres are K(-1/2)^2 with diagonal/twisted-diagonal image; scalar affine level index N or 2N','Proved','sections/B4.tex:B4.3','B4.2','138:35,40-41','Full GL2 affine index also explicit; adelic fibre index infinite; rank-one L4 true but full-fibre index 2 false'),
('B4.4','Independent elements of a number field have open scalar affine Kummer image with translation subgroup containing D Zhat^r','Proved under stated hypotheses','sections/B4.tex:B4.4','Schinzel1977 Thm2;MilneANT2020 Thm5.11;PeruccaSgobba2019 author preprint Thm1','138:20','D=|mu(K)| times saturation exponent; hypotheses hold for independent rational elements; full GLr ambient not open for r>=2')]
with (root/'notes/A3_B4_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes']);w.writerows(rows)
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, run /root/a3_b4'
events=[]
def event(id,typ,outcome):events.append((id,'2026-11-19',who,typ,outcome))
for row in rows:event(row[0],'targeted proof check',row[2]+': '+row[1]+'; exact scope: '+row[6])
for id in ['A3.1','A3.4','A3.5','B4.1','B4.2','B4.3']:
 event(id,'computation or formal certificate','code/a3_b4_verify.py; logs/a3_b4_verify.json and .txt; finite scope only, not a substitute for all-level proofs')
event('SA09-11 (138:19,36)','independent re-proof','B4.1 verifies index 2 at level 8 and proves exact all-level formula; no reliance on prior assertion')
event('SA09-11 (138:35-41)','used and rechecked in this run','B4.2-B4.3 derive fibre sign -1/2, contracted-product twist, and ax-b reciprocal action from Fermat coordinates')
event('SA09-11 (138:20)','used and rechecked in this run','B4.4 proves scalar-affine openness for independent rational elements and number-field extension; correct ambient group is essential')
event('SA09-4 (137:72)','carried as background without fault found','Only stated cohomology-product conclusion used to distinguish weak data; multiplicative-extension proof itself delegated elsewhere, not independently re-proved here')
event('SA09-5 (137:38-39)','targeted proof check','A3.2 supplies the full natural functor reconstruction posed there; does not assert weightwise PD deRham comparison alone proves it')
event('L2','independent re-proof','A3.1 identifies the universal cosimplicial tests; A3.2 constructs the full natural Gamma action and recovers tensor/unit from rho_2/rho_0; A3.3 derives full integral homotopy recovery. Mere cohomology operations are refuted by A3.4')
event('L4','independent re-proof','B4.1 proves literal index 2 assertion for K(2),K(1/2); B4.3 refutes extending that index to the full Fermat fibre ambient')
event('A3.1-A3.2','targeted proof check','Independent A2 agent checked ranks, variance, finite-free tensor/function comparison and normalized contraction; parent supplied and checked rho_2 cross-effect reconstruction')
event('B4.4','used and rechecked in this run','PeruccaSgobba2019 primary preprint Theorem 1 opened; its uniform degree bound independently implies scalar affine openness by bounded finite quotient indices')
event('B4.4','used and rechecked in this run','Complete Schinzel1980 corrigendum pp. 101-104 inspected; no correction changes the Theorem 2 statement used')
event('Belyi1979 (English translation 1980, §4 Thm4)','carried as background without fault found','Primary English PDF opened, Theorem 4 p. 255 and corollary p. 256; no A3/B4 proof depends on it')
with(root/'notes/A3_B4_CHECK_EVENTS.tsv').open('w',newline='')as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
print(json.dumps({'statements':len(rows),'events':len(events),'generated_utc':datetime.now(timezone.utc).isoformat()},indent=2))
