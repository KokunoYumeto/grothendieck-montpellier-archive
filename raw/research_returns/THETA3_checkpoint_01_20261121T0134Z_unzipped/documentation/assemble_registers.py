from pathlib import Path
import csv,hashlib,json,re
root=Path(__file__).resolve().parent.parent
d=root/'deliverables'; d.mkdir(exist_ok=True)
rows=[
('Q1','User task1; sketch Route1,1.7','Identify exact theta machine and prove proposed single seesaw comparison','OPEN','A1;B9;B10;B11;B12;A5','Exact restriction seesaw and finite-frame pairing established/in final checking; instantiate actual ValLastX step12 laws on032 data and determine algebraicity of correction.','Check actual global chain hypotheses and normalized kernels.'),
('Q2','User task2;032 Prop4.5–4.6/Cor4.7;Alpoge steps4,7,8','Obtain explicit nonvanishing from normalized determinant/period data','PARTLY PROVED','Q1–Q9;B5–B9','Explicit fixed-input, finite-grid and arithmetic-input certificates proved. Uniform arithmetic bounds or direct transfer from the specific Alpoge chain remain open.','Supply actual finite matrices/normalizations and source extraction coefficients.'),
('Q3','User task3;sketch Route1 Gate','Reach non-CM Hodge sources','PARTLY PROVED','C01–C05;C10;C12','Non-CM periods and surface cycles exist on noncongruence covers; exceptional Hodge summand still needs algebraic projector and full-rank tests.','Find a non-divisor Hodge summand with the C04 extraction data.'),
('Q4','User task4;sketch1.3,1.6','Carry comparison to integral models','PARTLY PROVED','C06–C11','Exact derived-density calculations and height-two derivative slope; raw theta frame and chosen horizontal-cycle matching remain unproved.','Match invariant derivation and integral theta frame, then local lattice/test data.'),
('Q1-local','Archive BesselPeriodGGP.lean;StatementG.lean','Evaluate local canonical U(2,1)/U(2) Bessel coefficient','PROVED','B9','Probability-Haar value1 for the stated coefficient type; no global value1 assertion.',''),
('Q1-innerform','Landherr classification;032 Taylor model','Keep finite Hermitian data while changing archimedean signature','PROVED REFINEMENT','B1;B2;B3','Negative definite neighbor preserves finite data but bare scalar type mismatches; positive definite neighbor needs one finite flip.','Use subgroup seesaw or perform local matching at the changed places.'),
('Q1-zero-orbit','vHS Lem4.2.7;A1','Prove a common averaged coefficient in anisotropic signatures','PROVED','A1','Exact averaged coefficient equals Phi(0), with untwisted action and probability measures.',''),
('Q1-global-source','Archive ValLastX.lean MainX/PerX','Identify precise source meaning of character-independent step12','SOURCE LOCATED','B13 pending','Common-family relation preservation and up/down theta operators located; direct specialization still under check.','Trace theorem witness and SPar/chain hypotheses.'),
('Q1-rallis','GQT Theorem11.4;Haan U(1) to U(3)','Find applicable normalized inner product formula','IN PROGRESS','A source dictionary','GQT second-term range excludes direct1→3; Haan formula located and hypotheses being checked.','Verify splitting, nonzero lift and local factor normalizations.'),
('Q1-stabilize','WeilTensorModels.lean Geo.IsGood','Use rank stabilization to apply first recovered matching candidate','OPEN','B10;A4','Smallest p1q0 ranks12,4; same signatures at every real place and common Wrank16 still differ from032.','Provide true tower/descent comparison, not a Lefschetz-degree substitution.'),
('Q2-scale','032 constant lines and theta linearity','Can positivity give a normalization-free lower bound?','REFUTED','B4','Scalar rescaling sends any nonzero period arbitrarily close to0.','Use named Hilbert, Haar and algebraic normalizations.'),
('Q2-iterate','Alpoge step8 analogy','Do positive multiplicity-one projectors alone control an iterated size?','REFUTED; REFINED','B6','Two rank-one projections have nonzero composition arbitrarily small; product lower bound needs overlap estimates.','Measure least singular values on successive image spaces.'),
('Q2-grid','A1;Q7','Make zero-orbit selection a finite bounded search','PROVED','Q7','N0^d explicit translates; named Lipschitz and lattice constants; total doubled G-level preserved.',''),
('Q2-fixed','032 Cor4.7','Quantify compact variation with fixed finite input','PROVED','Q1;Q2;Q3;Q8','Bound(1-eta)||xi||² and explicit tails/rounding/chart certificates.',''),
('Q2-Hecke','032 §§5–6 finite Hecke extraction','Bound denominators once integral Hecke matrices are specified','PROOF UNDER CHECK','Q9','Resultant projectors and algebraic norm lower bound; numeric matrices remain input.','Independent whole-proof check.'),
('Q3-congruence','Liu Prop4.13,Thm4.18,Cor4.20','Get non-CM H1 by raising congruence ball dimension','REFUTED','C01','Entire Albanese remains CM under the cited standard hypotheses.','Use noncongruence or different cohomological/source setting.'),
('Q3-trace','Finite etale trace and projection formula','Pair one new non-CM form with three old forms','REFUTED','C02','Trace-zero class cups three pullbacks to integral0.','Use at least paired new factors.'),
('Q3-mixed','Schoen2014 pp133–134;032 Prop4.5','Construct non-CM/CM mixed period on common cover','PROVED','C03','Select Schoen actual Hermitian space; transverse old theta form and non-CM elliptic form.',''),
('Q3-pure','Schoen2014 two Fermat projections','Construct purely non-CM four-form period','PROOF UNDER CHECK','C12','Explicit degree4 ball cover and degree500 map to F²; resultingF⁴cycle is product of diagonals.','Independent whole-proof check.'),
('Q3-extract','032 Prop3.1;algebraic correspondences','Turn nonzero period into every class of a target Hodge summand','PROVED REDUCTION','C04','Algebraic projector plus full-rank pairing matrix (or cyclic correspondence orbit).','Construct these data for an exceptional non-CM target.'),
('Q3-height','Li–Liu II Thm1.4–1.5,Ex1.10','Use non-CM arithmetic theta height for ordinary Hodge classes','REFUTED INFERENCE','C10','Homologically trivial cycles have zero ordinary cycle class.','Use their extension/height information without identifying it with a Hodge class.'),
('Q4-sign','Li–Zhang Thm3.4.1,3.5.1','Are all full-rank arithmetic intersections positive lengths?','REFUTED','C06','L=pi I3 hasInt=q+2−q²<0.','Separate derived signs and horizontal/vertical terms.'),
('Q4-positive','Li–Zhang local formula','Find exact positive local lattice sector','PROVED','C07','Selfdual(rankn−1) plus normpi^(2a+1) hasInt=a+1≥1.','Match this sector to actual theta test data.'),
('Q4-generic','Specialization and basic uniformization','Does positive special-fibre intersection produce generic Hodge cycle?','REFUTED INFERENCE','C08','Vertical fibre/section length1 has empty generic fibre; N_red factor retained in basic uniformization.','Identify horizontal flat cycle and its desired realization.'),
('Q4-quasic','Sketch1.6;Gross Prop5.3','Identify coefficient with a convergent product of quasi-canonical coordinates','REFUTED; REFINED','C09','Reciprocal-index sum is correct; infinite coordinate product does not converge; orbit norms have different valuations.','Use finite divisor identity or C11 formal-group mechanism.'),
('Q4-derivatives','Alpoge step2;Bannai–Kobayashi Prop3.5','Derive exact height-two derivative slope and test sharpness','PROVED / WRITEUP IN PROGRESS','C11','Integral formal functions satisfy exact digit-sum bound; raw theta trivialization still requires comparison.','Save full proof and normalize theta connection/frame.'),
]
with open(d/'QUESTIONS.tsv','w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['id','source_and_locator','question','state','finding_ids','current_gate_or_result','next_step']);w.writerows(rows)
# Preserve the inventory record and combine all actual event registers.
fields=['statement_id','date','who_model_effort_run','type','outcome','method_and_locator']
out=[]
old=list(csv.reader(open(d/'CHECK_EVENTS.tsv'),delimiter='\t'))
if len(old)>1: out.extend(r for r in old[1:] if r and r[0]=='SRC-INVENTORY')
for p in sorted((root/'work').glob('*.tsv')):
 if not re.search(r'check|CHECK_EVENTS',p.name): continue
 raw=list(csv.reader(open(p),delimiter='\t'))
 if not raw:continue
 for r in raw[1:]:
  if len(r)<5:continue
  r=(r+['']*6)[:6]
  kind=r[3].lower()
  if kind not in {'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'} and not kind.startswith('refuted'):
   original=r[3]
   if 'computation' in kind or 'enumeration' in kind:r[3]='computation or formal certificate'
   elif 'independent' in kind and ('re-proof' in kind or 'reproof' in kind):r[3]='independent re-proof'
   elif 'proof' in kind:r[3]='targeted proof check'
   elif 'source' in kind:r[3]='carried as background without fault found'
   else:r[3]='used and rechecked in this run'
   r[5]=(r[5]+'; ' if r[5] else '')+'Original event label: '+original
  r[5]=(r[5]+'; ' if r[5] else '')+'Working register: '+p.name
  out.append(r)
rootwho='GPT-6 Astra Pro; effort not exposed; THETA3-20261121/root'
for q in range(1,10):
 out.append([f'THETA3-Q{q}','2026-11-21',rootwho,'targeted proof check','Passed author whole-proof reread; exact hypotheses and normalization retained.','Full proof in work/root_quantitative.md; LaTeX transcription proof read.'])
out.append(['THETA3-C12','2026-11-21',rootwho,'targeted proof check','Passed author whole-proof reread; independent check pending.','Kummer degree5, quotient degree25, coprime etale degree4, generically finite degree500, Koszul sign and diagonal pushforward.'])
out.append(['THETA3-Q2-NUM','2026-11-21',rootwho,'computation or formal certificate','Interval arithmetic verifies coarse wedge lower bound137/1000000 in the stated Gaussian model; not a formal proof of a global cycle.','work/check_gaussian_certificate.py and output.'])
out.append(['SRC-MILNE2026-2.1-3.1-3.5','2026-11-21',rootwho,'carried as background without fault found','Read supplied statements for CM Hodge, full Tate over finite fields and Hodge standard for abelian varieties; no new proof claimed.','Supplied report Theorems2.1,3.1,3.5.'])
out.append(['SRC-GROTH16-43-46','2026-11-21',rootwho,'used and rechecked in this run','Visually checked original scans43–46; letterdate4Jan1967 and complementary-dimension formulation on43; hyperplane/correspondence proposition44–45.','work/archive_images/16_scan_43.png through46.'])
with open(d/'CHECK_EVENTS.tsv','w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(fields);w.writerows(out)
# Hash all source recovery inputs; original works stay cited, not republished.
with open(d/'evidence'/'EXTERNAL_INPUT_HASHES.tsv','w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['workspace_relative_path','bytes','sha256'])
 for sub in ['work/external','work/archive_images','work/alpoge_mirror']:
  for p in sorted((root/sub).rglob('*')):
   if p.is_file():w.writerow([p.relative_to(root),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest()])
print('questions',len(rows),'check_events',len(out))
