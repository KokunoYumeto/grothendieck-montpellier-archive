from pathlib import Path
import csv,json,datetime
R=Path('work/complexity');now=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
rows=json.loads((R/'rows.json').read_text())
fields=['statement_id','date','who','model','effort','run','type','outcome']
events=[]
def event(i,t,o):events.append([i,now,'/root/complexity','GPT-6 Astra Pro','not exposed','GRH_NIGHT/complexity',t,o])
new={'CX-ALG-005','CX-ALG-014',*[f'CX-GEO-{i:03}' for i in range(1,7)]}
carried={'CX-ALG-003','CX-ALG-004','CX-ALG-006','CX-ALG-008','CX-ALG-009','CX-ALG-010','CX-ALG-011','CX-ALG-012','CX-ALG-013','CX-HN-002','CX-HN-003','CX-HN-004','CX-NN-001','CX-NN-002','CX-NN-004','CX-LIM-002'}
for row in rows:
 i=row['id']
 if i in new:
  event(i,'targeted proof check','Read the complete written statement and proof in section.tex after drafting. Checked all quantifiers, encoding sizes, edge cases and claimed analytic inputs. No gap found. This is a model reading, not formal verification.')
 elif i in carried:
  event(i,'carried as background without fault found','Matched to exact attached run/statement locator and preserved all hypotheses. Prior full proof text is not in tonight’s attachment where noted; no fresh independent whole-proof certification claimed.')
 else:event(i,'used and rechecked in this run','Checked statement/input classification against cited available source or exact current reduction; no unrecorded proof audit claimed.')
for i in ['CX-ALG-014','CX-GEO-005']:
 event(i,'computation or formal certificate','Exact Python integer/finite-field check in check_finite_examples.py; results finite_checks.json. For GL3(F2), all168 invertible matrices checked; stabilizer has24 elements and no common nonzero fixed covector. Not a kernel/formal certificate.')
for src in json.loads((R/'sources.json').read_text()):
 t='carried as background without fault found' if src['id'] in {'CX-S-BACH','CX-S-GSS'} else 'used and rechecked in this run'
 event(src['id'],t,src['inspection'])
for i in ['SGA1-V-7','SGA3-VIII-1.1-1.2','SGA4-IX-3.2','SGA4-IX-3.3','SGA6-V-3.10','SGA6-VI-3.2-3.3','EGAII-6.1.4-6.1.5','ARCHIVE-28-SCAN3','ARCHIVE-98-SCANS11-12','ARCHIVE-98-SCAN44','ARCHIVE-2-SCAN5']:
 event(i,'carried as background without fault found','Geometric/archive companion locator carried from RETURN_CX_GRH_final_IMPLICATIONS.md §4 and intake; original SGA/EGA pages or archive scans not freshly inspected here. No claim that archive states a modern complexity theorem.')
for i in ['CX_GRH-CX-K01','CX_GRH-CX-K02','CX_GRH-CX-K03','CX_GRH-CX-K04','CX_GRH-CX-K05','CX_GRH-CX-K06','CX_GRH-CX-K07','CX_GRH-CX-N01','CX_GRH-CX-N02','CX_GRH-CX-N03','CX_GRH-CX-N04','CX_GRH-CX-N07','CX_GRH-CX-N08','CX_GRH-CX-N13','CX_GRH-CX-N14','CX_GRH-CX-N15','CX_GRH-CX-U02','CX_GRH-CX-U03','ALPOGE_GCT-C-GRH-02','ALPOGE_GCT-C-GRH-03','ALPOGE_GCT-P-F7','ALPOGE_GCT-P-F10','PLETH-PLE-F5','PLETH-PLE-F7']:
 event(i,'carried as background without fault found','Attached implications/questions/intake read and matched; retained as prior finding, not new in this run. The source proof is not fully reproduced by the supplied attachment.')
for i in ['MT-ART01','MT-ART02']:
 event(i,'targeted proof check','Independent agent read entire root proof in work/root/section.tex. MT-ART01 matched fresh Khare–Wintenberger Cor10.2(ii), authorPDF21, and Brauer transfer; MT-ART02 checked exact convolution spectrum, cyclic restriction orders, and top-field zeta identity. No gap found. Added S4 representation-theoretic counterexample communicated to root.')
with (R/'events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(fields);w.writerows(events)
q=[
('CX-Q01','Bach1990T2/3; Schoof2008T2.2; CX_GRH CX-N01','Which primality and prime-field tasks are actually discharged by A_D?','proved: CX-ALG-001,003–008; PRIMES-in-P historical attribution corrected by CX-ALG-002'),
('CX-Q02','HAC Algorithm3.34 p100','Does A_D derandomize prime-field square-root extraction?','proved: CX-ALG-005'),
('CX-Q03','Proposed witness-to-factor shortcut','Does a Miller witness always yield a factor by its immediate three gcds?','refuted: CX-ALG-014, N=35,a=2,m=17'),
('CX-Q04','CX_GRH CX-N15/CX-U02','What is the strongest available general finite-field factorization transfer?','proved conditional on M: CX-ALG-009; A_D-only extension gate CX-ALG-010 (high valuation coefficient unit or alternative descent)'),
('CX-Q05','Bach1990T4; CX_GRH CX-N07/N08','What does GRH give for class groups and what computation remains?','proved conditional generator transfer CX-ALG-011/013; full polynomial relation-search bound remains gate CX-ALG-012'),
('CX-Q06','Koiran DIMACS§2T2,§5T9/C1,1997erratum','Which field zeta input suffices for HN∈AM?','proved/classically located: CX-HN-001/002; M supplies it'),
('CX-Q07','CX_GRH CX-K03/K04; ALPOGE_GCT C-GRH-03','Can the HN solution field always be replaced by an abelian one?','refuted universal replacement: CX-HN-004 x³−2; bounded promise transfer proved CX-HN-003'),
('CX-Q08','HN consequence, constructible formulas','Does existential Boolean constructible feasibility preserve AM?','proved conditional on M: CX-GEO-001'),
('CX-Q09','Rabinowitsch principal-open reduction','What does M give for radical membership?','proved conditional on M: CX-GEO-002'),
('CX-Q10','Explicit equations for X,Y','What does M give for inclusion/equality of reduced algebraic sets?','proved conditional on M: CX-GEO-003; scheme-theoretic ideal inclusion not asserted'),
('CX-Q11','Bach–Sorenson1996T5.1 p1729','How many primes suffice to distinguish unequal finite permutation characters while avoiding S?','proved conditional on stated zeta input: CX-GEO-004, explicit bounds CX.2–CX.4'),
('CX-Q12','Galois-category linearization','Do equal permutation characters force isomorphic transitive G-sets?','refuted: CX-GEO-005, natural and dual7-element GL3(F2)-sets'),
('CX-Q13','Explicit algebraic group action','Does M place orbit membership in AM without computing orbit equations?','proved conditional on M: CX-GEO-006; orbit-closure boundary remains separate'),
('CX-Q14','GCT V T3.4; CX_GRH CX-K05','What normalization-map complexity is established?','proved inherited conditional refinement CX-NN-001; historical EXPH and equation-access distinctions CX-NN-002/004; earlier unconditional PSPACE CX-NN-003'),
('CX-Q15','GCT V T4.7/L4.8; PIT/BPP questions','Do the cited GRH transfers close general derandomization or GCT hardness gates?','current gate: CX-LIM-001, uniform hitting sets or independent border-hardness theorem; no logical nonimplication claimed'),
('CX-Q16','ALPOGE_GCT P-F7/P-F10 and PLETH PLE-F5/F7','Does positivity/purity remove efficient multiplicity-construction gates?','specified earlier counterexamples carried CX-LIM-002; actual quotient ranks and uniform data construction remain'),
('CX-Q17','CX_GRH separate premise E','Are the preceding ETH deductions consequences of tonight’s two inputs?','proved input classification CX-LIM-003: those proofs require separate E'),
('CX-Q18','Root MT-ART01/02','Do the proposed odd Artin and finite-kernel reductions pass an independent full reading?','targeted whole-proof checks passed, recorded in events.tsv; no independent formal proof claim')]
with (R/'questions.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['id','source_and_locator','question','state']);w.writerows(q)
print('Wrote',len(events),'events and',len(q),'questions at',now)
