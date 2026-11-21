"""Integrate the frozen checked F59 singular-factor/pure-coefficient amendment."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,csv
r=Path(__file__).resolve().parent
report='agent_soergel_scalar_amendment.md';rs='56022996637e174e50382b3d8cf76ea7f4c3a08900783996bd29dab59e350ebf'
frag='finding_F59_scalar_amendment.tex';fs='0edcea01cf3a63495928e4a8b218f1fb37a43dc628291d5ccfb1b5be41e909fa'
review='REVIEW_SOERGEL_SCALAR_AMENDMENT_GCT.md';vs='42b1c6582f08698902852873f2e91b773d760aded358582a336ad635511fed6a'
for n,h in [(report,rs),(frag,fs),(review,vs)]:assert hashlib.sha256((r/n).read_bytes()).hexdigest()==h
assert fs in (r/review).read_text()
p=r/'GCT_NSRH.tex';s=p.read_text();assert r'\label{f:pureScalarSoergelNoGo}' not in s
body,dictionary=(r/frag).read_text().split('% Separate paragraph for Part III.',1)
anchor=r'\subsection{Bounded kernels, finite-algebra characters, and an actual word relation}'
assert s.count(anchor)==1;s=s.replace(anchor,body.rstrip()+'\n\n'+anchor)
anchor=r'\section{Archival audit and the Fable leads}\label{sec:archive}';s=s.replace(anchor,dictionary.strip()+'\n\n'+anchor)
s=s.replace('excludes every lift with flat cohomology. F62 constructs','excludes every lift with flat cohomology. The natural singular-invariant correspondence also fails after any bounded scalar coefficient change. Moreover the pure scalar quadratic coefficients of F61 cannot transfer into this ordinary-Hecke category, even with nonflat cohomology: their outer cohomological multiplicities are odd, contrary to the generic support criterion. F62 constructs')
p.write_text(s)
q=r/'QUESTIONS.tsv'
with q.open(newline='') as f:rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for x in rows:
 if x['id'] in ['Q3-GCT','Q3-ALTERED-SCALAR-HECKE','Q3-BOUNDED-ORDINARY-HECKE']:
  x['current_gate']+=' The scalar multiple U⊗(A⊗_{A^tau}A) fails for every bounded scalar coefficient by9r²≠6r² at the origin. Pure scalar coefficients with the actual three-root D trace have dimensions1,2,1 in distinct degrees and violate generic degreewise evenness, even without flatness of X.'
 if x['id']=='Q3-ALTERED-SCALAR-HECKE':
  x['state']='UNIFORM_SUPPORT_PROVED; FLAT_COHOMOLOGY_SINGULAR_FACTOR_AND_PURE_D_REPAIRS_REFUTED'
  x['next_step']='Investigate a genuinely nonfactorable nonflat complex with a mixed scalar coefficient outside the tested pure arithmetic law, or change the category/map.'
with q.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
now=datetime.now(timezone.utc).isoformat()
with (r/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['F59-SCALAR-AMENDMENT-ROOT',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','targeted proof check','Original whole report, complete final delta and entire final fragment read/reconstructed; top-degree singular-fiber and pure degreewise-evenness contradictions PASS.','ROOT_REVIEW_F63_F64_SC_AMENDMENT.md; '+report+' SHA256 '+rs+'; '+frag+' SHA256 '+fs]);w.writerow(['F59-SCALAR-AMENDMENT-FRESH',now,'/root/gct_statements','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','independent re-proof','Whole report, dependency SC-A and complete fragment checked; exact BBD5.1.8 context reread; PASS.',review+' SHA256 '+vs])
with (r/'LEDGER.md').open('a') as f:f.write('\n## '+now+' — stronger altered-scalar tests integrated\n\nThe entire checked F59 amendment now excludes every scalar-complex multiple of the singular invariant correspondence, for arbitrary bounded scalar coefficient. It separately excludes the natural pure D coefficient transfer from F61 into the ordinary bounded Hecke category without any flatness hypothesis on the lift. The remaining scalar escape must be nonfactorable, nonflat and outside the specified pure arithmetic comparison. This is not a failure of F61 in its distinct finite-state category.\n')
with (r/'IMPLICATIONS.md').open('a') as f:f.write('\nThe stronger F59 scalar tests exclude the explicit singular correspondence after arbitrary scalar changes and exclude any pure coefficient having the actual three-root D trace. The latter uses the actual dimensions1,2,1, not a false retention of generic internal grading. Hence the existing pure finite-state coefficients cannot simply be transported into the ordinary-Hecke lift. A possible altered-scalar repair must contain genuinely nonfactorable nonflat cohomology and a different mixed coefficient comparison.\n')
print('F59 scalar amendment integrated',hashlib.sha256(p.read_bytes()).hexdigest())
