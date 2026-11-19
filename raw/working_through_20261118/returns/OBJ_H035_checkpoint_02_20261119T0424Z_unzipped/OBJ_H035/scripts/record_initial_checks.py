from pathlib import Path
import csv,datetime
r=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
readings=[
('003','18–20','completion comparison','Finite modules over the completed ring, not only completions of finite A-modules','The hat belongs to the ring in the finite-module condition','Retain literal completed-ring quantifier','high'),
('004','19–20','every quotient B; nonnilpotent f','B must be nonzero','No nonzero qualification visible at this locus','Record zero-ring boundary correction separately','medium-high'),
('006','22','f in A/p','f nonzero in the integral quotient','No nonzero restriction visible; enlarged original crop inspected','Retain written text; correct theorem explicitly excludes zero','high'),
('008','18','F(N) est de type fini','Such finiteness would be needed for the converse','The enlarged crop clearly invokes finite generation of F(N)','Proof invokes an unstated assumption; do not add it to the ink','high'),
('009','6;16','M','The coherent coefficient F','Undefined M in the displayed proof','Record a notation slip, keep the statement with F','high'),
('010','9','Hom(L_i,P)','Coefficient Q in the Hom complex','P is written; compare the surrounding coefficient notation','Literal formula false; correction marked ours','high'),
('010','15','Tor_1(M,Z^1(K))','Tor_1(M,B^1(K)) or a stronger all-positive-Tor condition','Enlarged crop shows Z^1, not B^1','Retain Z^1 and refute the literal criterion','high'),
('011','1','module de différentielles pour un C.M.','Canonical/dualizing module fits the quotient property','Enlarged header reads différentielles','Do not replace by dualité; canonical interpretation explicitly reconstructed','high'),
('011','17m','excellent; EGA IV 6.11.8','Generic canonical modules require more than CMU','Margin gives both excellent and the EGA reference','Separate valid excellent claim from false CMU extension','high'),
('013','8–20','cancelled Corollaire 11','Final rewritten Phi_R(M)=Hom(R,M)','Diagonal cancellation and local deletions are visible','Treat as a cancelled draft, not an uncancelled theorem','high'),
('015','1–9','strict in cancelled draft; absent in rewrite','Strict finite projective system','Strictness is not repeated in the rewritten statement','Explicit stationarity assertion needs restored hypotheses','high'),
('016','23','B non nul','Nonzero quotient required for nonnilpotent f','Enlarged crop shows inserted non nul over B','Retain insertion as part of the statement','high'),
('020','10–16','R inserted; Tor(F); gr O_X','Tor(R), and generic freeness for gr R too','The proof changes letters and only names gr O_X','Record notation and proof omissions separately','high'),
('021','3','forall s in S','s in the dense open U','Enlarged crop confirms S','Keep literal S; exhibit counterexample and prove U version','high'),
('022','1–8','additif ?; proposed composition','A precise additive A-linear category and a closure proof','Question mark and prospective language are visible','Keep programme and its unresolved exact scope separate from modern coherent functors','high'),
('023','21','Hom(F,O_X tensor M)','f_* Hom on the base S','The displayed formula omits the pushforward','Correct the type mismatch explicitly','high'),
]
with (r/'READINGS.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['cote','scan','line','reading','what_the_mathematics_expects','scan_shows','decision','confidence'])
 for row in readings:w.writerow(['94',*row])
with (r/'CHECK_EVENTS.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['id','date_utc','who','how','result','where'])
 for n in range(1,16):
  w.writerow([f'H035.{n}',now,'GPT-6 Astra Pro; effort not exposed; OBJ_H035 single-stream run','targeted proof check','First proof/counterexample drafted; independent recheck pending',f'PROOFS.tex section H035.{n}'])
 for key,where in [('Stacks08Z9','Proposition 47.7.8, lines 23–28 of opened tag'),('Stacks0B5A','Lemma 47.16.7, lines 23–35 of opened tag')]:
  w.writerow([key,now,'GPT-6 Astra Pro; effort not exposed; OBJ_H035 single-stream run','used and rechecked in this run','Exact hypotheses and conclusion read; completeness/dualizing-complex hypotheses retained',where])
print(f'Recorded {len(readings)} decisive readings and 17 conservative check events at {now}.')
