from pathlib import Path
import csv,datetime,shutil
root=Path(__file__).resolve().parent.parent
out=root/'deliverable';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
cols=['statement_id','date_utc','who','model','effort','run','type','outcome','detail','source_locator']
events=[]
for src in ['fields_literature','sdp_orbits','pencil','root']:
 p=root/'work'/src/'CHECK_EVENTS.tsv'
 with p.open(newline='') as f:
  for row in csv.DictReader(f,delimiter='\t'):
   clean={k:row.get(k,'') for k in cols}
   clean['date_utc']=row.get('date_utc') or row.get('date','')
   clean['detail']=row.get('detail') or row.get('method_or_locator','')
   if row.get('source_sha256'):clean['detail']+='; source_sha256='+row['source_sha256']
   events.append(clean)
# Dates below identify checks already performed in this run; no invented timestamps.
def add(ids,kind,detail,locator='',outcome='PASS',date='2026-11-21'):
 for sid in ids:
  events.append(dict(zip(cols,[sid,date,'/root','GPT-6 Astra Pro','inherited; no separate numeric effort exposed','BR_PENCIL-20261121-R1',kind,outcome,detail,locator])))
add(['R-01'],'targeted proof check','Read complete proper-incidence proof: local regular frames, closed flag projection, support reduction, atom-span intersection and extension from actual rank to border rank; arbitrary residual order and fields checked.','sections/substitution.tex R-01')
add(['P-01','P-02','P-03','P-04','P-05','P-06','P-07'],'targeted proof check','Read complete proof in author notes and integrated TeX; checked torus weights, leading frames, coordinate projections and indicated degeneration or compression.','work/pencil/PENCIL_PROOFS.md; sections/pencils.tex')
add(['FL-01','FL-02','FL-03','FL-04','FL-05'],'targeted proof check','Read complete author proof and integrated field conventions; unit coefficients, divided powers, complement projections, proper closure and ordinary-power factorial obstruction checked.','sections/fields.tex')
add(['S-01','S-02','O-01','O-02'],'targeted proof check','Read full proof and examples, checking exact rational witness, separable perturbation algebra, orbit attainment, polar decomposition, convexity and balanced projector.','sections/sdp_orbits.tex')
add(['R-04'],'targeted proof check','Read complete unique-extension/prolongation proof and standalone verifier. Checked limiting-span incidence, all five unit minors, annihilator and kernel equalities and final rank82>80 contradiction.','sections/permanent_apolar.tex')
add(['R-06','R-07'],'targeted proof check','Read full uniform_n.tex proof independently; verified support classification, five graph orbit counts, characteristic transfer, anchored upper bounds and monotonicity argument.','sections/uniform_n.tex')
add(['R-02','R-03','R-05'],'computation or formal certificate','Executed independent exact integer-minor/orbit audit, including strengthened determinant unit minor. No floating point and no formal theorem prover.','work/pencil/root_certificate_audit_strengthened.json')
add(['R-04'],'computation or formal certificate','Executed standalone standard-library Bareiss verifier; K40=+1,L50=-1,H35=-1,E10=+1,R82=-1; LK=0 and HE=0.','checks/check_permanent_apolar_certificate.py')
add(['S-01'],'computation or formal certificate','Reran exact SymPy primal/dual identity, Gram eigenvalues, product objective and tensor rank-three identity.','checks/check_certificates.py')
add(['GCT_GINEQ:check_tensor_decompositions','GCT_GINEQ:agent_sdp_checks'],'used and rechecked in this run','Reran the two supplied predecessor scripts successfully. This event records computation only, not a new complete read of every predecessor proof.','source/RETURN_GCT_GINEQ_final_20261120T2340Z/checks/')
add(['P-09'],'targeted proof check','Read complete two-type prolongation proof and all verifier code; checked torus fixed limit, saturation kernel inequality, annihilator necessity, line-column weight distinction and overlap argument. Individual char0 cases only.','sections/det7_two_type.tex')
add(['P-09'],'computation or formal certificate','Ran independent exact modular verifier:1095+50 choices,1089 saturation minors,3353 linear zero-pattern tests; all PASS; no global mu7=14 inference.','checks/verify_det7_certificate.py')
add(['P-12'],'targeted proof check','Read whole P12 proof; verified application of P09 criterion and baseline74 plus minimum increment5 over all homogeneous line choices.','sections/det7_extra_m12.tex')
add(['P-12'],'computation or formal certificate','Executed updated independent verifier with P12 file:108 saturation minors,140 zero-pattern tests and baseline/annihilator identities PASS.','checks/verify_det7_certificate.py --certificate det7_extra_m12_certificate.json')
add(['P-10','P-11'],'targeted proof check','Read full finite-difference and cubic-pencil proofs; checked coefficient extraction, cost3 double-Koszul map, characteristic scope, initial9-term upper identity and rowP4 rank8 corollary; the revised exact8 determinant proof is recorded in a later event.','sections/adjacent_cubic.tex')
summary=out/'checks/verification_summary.json'
if summary.exists():
 import json
 d=json.loads(summary.read_text())
 for check in d['checks']:
  add([check['finding']],'computation or formal certificate','Executed packaged checker from its final relative location; '+check['log']+'; exact arithmetic, not a formal theorem prover.','checks/'+check['checker'],check['status'],d['date_utc'])
with (out/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader();w.writerows(events)
questions=[
('Q-01','BR_PENCIL prompt task1; intake5.1b','General Grassmannian residual minimum on the four families','PROVED REDUCTION','P-01; R-01','Exact finite reduction to coordinate subspaces; numerical values beyond the stated parameter ranges remain separate gates.'),
('Q-02','BR_PENCIL prompt task1, n=4,b=2,j=2','Exact requested residual pencil minima','PROVED','P-03; P-04; P-05','Row minima3; polynomial minima6; corresponding lower bounds7 and40.'),
('Q-03','BR_PENCIL prompt main aim','A polynomial det4/per4 border-rank lower bound above39','PROVED','R-02; R-03; R-04; R-05; R-08; R-10','Both CP border ranks at least43 in characteristic zero and at least42 over every algebraically closed field in the integral model; usual complex symmetric border ranks also at least43.'),
('Q-04','Continuation of task1, retained dimensions3 through6','Exact polynomial residual minima for j=3,4,5,6','PROVED','R-02; R-03; R-04; R-05; R-06; R-07','Minima8,9,11,12 for every n>=4.'),
('Q-05','Continuation of task1, row b=2','Row quadratic residual minima','PROVED IN STATED RANGES','P-03; R-06; P-20','Permanent minimum j+1 for every1<=j<=binom(n,2), all fields. Determinant minimum j+1 in the star range1<=j<=n-1; larger determinantj remains a separate numerical question.'),
('Q-06','Task1 for b>2; P-02','Numerical value of the adjacent two-plane seed for residual order b>2','CURRENT GATE','P-02; P-10; P-11','Row b3 seed is6 for the permanent in all fields,8 for determinant outside characteristic2 and6 in characteristic2. Polynomial b3 seed has the separate P-18 gate. General b numerical formula remains open.'),
('Q-07','Continuation of main aim; seven-dimensional residuals','Can substitution improve42 to43?','PROVED','R-08; R-09; R-10; P-09; P-12; P-13; P-14; P-15; P-16; P-19','Both seventh minima equal14 in characteristic zero; eighth and ninth equal15 and16. Complete finite coverage and all required prolongation certificates give43 for both full polynomial tensors.'),
('Q-08','BR_PENCIL task2; GCT_GINEQ Q-30','One residual image outside four families with exact DPS alpha and error','PROVED','S-01; S-02','Explicit concise2x2x3 residual image hasalpha3/4; rational PPT certificate; zero gap at every higher PPT Bose level.'),
('Q-09','GCT_GINEQ Q-30 beyond requested example','Generic efficient certified alpha algorithm','CURRENT GATE','','The supplied example does not settle generic complexity; dimension-dependent hierarchy error is proved, efficient generic optimization is not.'),
('Q-10','BR_PENCIL task3; GCT_GINEQ F-18,F-22,F-23','F-23 over every algebraically closed field','PROVED','FL-01; FL-02; FL-03; FL-04; FL-05','Properness proof and unit integral coefficient tensors; ordinary polynomial powers in p<=n distinguished and refuted as a finite-rank convention.'),
('Q-11','BR_PENCIL task4; intake5.4; GCT_GINEQ F-19','Orbit-invariant maximum of alpha through Kempf-Ness','REFUTED; REFINED','O-01; O-02','Product-GL supremum always1; maximum absent on product-free spaces. Kempf-Ness concerns Plucker norm minimization and scalar projector marginals.'),
('Q-12','BR_PENCIL task5','Compare against post-2015 bounds and border apolarity','CHECKED SCOPE','Literature section; FL-06','Primary source audit completed for listed works. No historical-priority theorem claimed; survey misstatement refuted by degree-two example.'),
('Q-13','BR_PENCIL language-of-results requirement','Transfer each finding to Grothendieck frameworks with exact locators','PROVED DICTIONARY; ARCHIVE LIMIT EXPLICIT','Dictionary part','Published EGA/FGA/SGA locators and verified scan leaves supplied. No manuscript cote supporting modern findings established; none invented.'),
('Q-14','S-02','Dimension-dependent DPS projector error','PROVED','S-02','0<=beta_k-alpha<=(d-1)/(k+d-1), from the precise Bose-extension convention and NOP Theorem2 equation7.'),
('Q-15','Dutta-Lysikov arXiv2510.13049v1 section4.3 p29 afterCor56','Literal border-Waring lower display binom(2n,n)','REFUTED','FL-06','Atn2, det2 andper2 are nonsingular quadrics of symmetric border rank4, below6; four-square identity and matrix lower bound supplied.')]
questions.extend([
('Q-16','P-02; continuation of task1 at b=3,j=2','Exact polynomial cubic adjacent-pencil minimum','CURRENT GATE','P-18','Permanent21..24 in every characteristic; determinant21..27 outside characteristic3, with common21..24 interval in characteristic2. Determinant lower21 in characteristic3 remains uncertified. The proved upper bounds cap this substitution at38 for permanent and41 for determinant.'),
('Q-17','Continuation of main aim after R-08/R-10','Can ten retained dimensions raise the n4 bound to44?','CURRENT GATE','R-07; R-08; R-10; P-17; P-20','Permanent mu10 lies in17..18. Determinant reduces to59 Borel ideals:6 Koszul cases and18 P-17 cases are excluded at17, leaving35 ideals. Additional extension-space refinements are exploratory until separately certified. No global44 theorem yet.'),
('Q-18','Continuation of R-06 and R-08/R-10','Does the exact seventh minimum14 hold for every n>=4?','PROVED','R-11','Both seventh minima equal14 in characteristic zero for everyn>=4; eighth and ninth equal15 and16. Exact34-graph cover,1027 subsetorbits,18501 support-exact subsets and4996 modular minors verify all additional cases. Full polynomial lower bound binom(n,2)^2+7.')])
questions.append(('Q-19','Continuation of main aim via P-02 b=3,j=2','Can the cubic two-plane substitution improve the size-four bound43?','REFUTED FOR THIS ROUTE','P-18','Explicit/integral upper bounds cap the determinant result at41 and the permanent result at38 over every algebraically closed field. Exact cubic pencil values remain Q-16, but cannot improve43 by this route.'))
with (out/'QUESTIONS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['id','source_and_locator','question','state','finding_ids','current_gate_or_resolution']);w.writerows(questions)
print('Wrote',len(events),'check events and',len(questions),'question rows at',now)
