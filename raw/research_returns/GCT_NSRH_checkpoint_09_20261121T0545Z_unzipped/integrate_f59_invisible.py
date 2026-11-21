from pathlib import Path
from datetime import datetime,timezone
import hashlib,csv
r=Path(__file__).resolve().parent
rep='agent_soergel_invisible_summand_gate.md';rs='f3db729bc2006d4f23b2d1a84d31cb6512cb1ef8d58a24d6a292ba48f3f09b84'
frag='finding_F59_invisible_summand.tex';fs='41fa377d5536c2fd3dec25179cd051339f84a80b05d0119bea11ad462153a61a'
review='REVIEW_INVISIBLE_SUMMAND_GCT.md';vs='b5672cab6b2c598afeb3a1d7e51e56d4fde3478015f2109f80a31e6824be389e'
for n,h in [(rep,rs),(frag,fs),(review,vs)]:assert hashlib.sha256((r/n).read_bytes()).hexdigest()==h
assert fs in (r/review).read_text()
p=r/'GCT_NSRH.tex';s=p.read_text();assert r'\label{f:invisibleSummandNoGo}' not in s
body,dictionary=(r/frag).read_text().split('% Separate paragraph for Part III.',1)
a=r'\subsection{Bounded kernels, finite-algebra characters, and an actual word relation}';s=s.replace(a,body.rstrip()+'\n\n'+a)
a=r'\section{Archival audit and the Fable leads}\label{sec:archive}';s=s.replace(a,dictionary.strip()+'\n\n'+a);p.write_text(s)
q=r/'QUESTIONS.tsv'
with q.open(newline='') as f:rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for x in rows:
 if x['id']=='Q3-ALTERED-SCALAR-HECKE':
  x['current_gate']+=' A generically acyclic correction cannot be added as an actual direct summand of a global free two-graph part: positive derived-origin dimensions force that correction to vanish. Nonsplit coupled extensions remain outside this argument.'
  x['approaches_tried']+='; positive derived-origin size and invisible direct-summand rigidity'
with q.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
now=datetime.now(timezone.utc).isoformat()
with (r/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['F59-INVISIBLE-ROOT',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','targeted proof check','Entire report and complete final fragment read/reconstructed: precise graph localization, finite positive derived fiber, top-degree graded Nakayama, twist invariance and direct-sum dimension cancellation PASS.',rep+' SHA256 '+rs+'; '+frag+' SHA256 '+fs]);w.writerow(['F59-INVISIBLE-FRESH',now,'/root/gct_statements','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','independent re-proof','Whole report and entire final fragment checked and matched; exact category and nonsplit-extension limit retained; PASS.',review+' SHA256 '+vs])
with (r/'LEDGER.md').open('a') as f:f.write('\n## '+now+' — invisible direct-summand repair excluded\n\nF59 now includes the full checked derived-origin-size proof. An actual direct summand generically invisible cannot repair a free graph part with the required generic quadratic; it must vanish. This does not split nonsplit extensions or close the full mixed/nonflat case. New rank-one module rigidity remains a separate active investigation and is not asserted in the paper.\n')
print('Invisible-summand proof integrated',hashlib.sha256(p.read_bytes()).hexdigest())
