from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
r=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rep='agent_soergel_quotient_route_tests.md';rh='d50900b1353ce0c01b43832283e7ea9464d976dac2e7853f7053004ee9014e9e'
frag='finding_F59_quotient_tests.tex';fh='a6a354fc2ae0cb7f198709a746dd6ab648bb8ce7463c13f2b78d3cb4e3948265'
rev='REVIEW_SOERGEL_QUOTIENT_ROUTES_GCT.md';vh='3f767a184ebcad62942bb62c5b2293fd5e59308c048a63d135fe9fbeffe33d85'
for n,h in [(rep,rh),(frag,fh),(rev,vh)]:assert sha(r/n)==h,n
assert fh in (r/rev).read_text() and 'PASS' in (r/rev).read_text()
p=r/'GCT_NSRH.tex';assert sha(p)=='0562c87d3d8efa533d9901a2d1c690a214d8d60411d27b414442eccd94fff645'
s=p.read_text();body,dictionary=(r/frag).read_text().split('% Separate paragraph for Part III.',1)
anchor=r'\subsection{Bounded kernels, finite-algebra characters, and an actual word relation}'
da=r'\section{Archival audit and the Fable leads}\label{sec:archive}'
assert s.count(anchor)==s.count(da)==1
s=s.replace(anchor,body.rstrip()+'\n\n'+anchor).replace(da,dictionary.strip()+'\n\n'+da)
needle='An explicit different-class example shows that central non-scalar quadratics do exist; it is not the required lift.'
assert needle in s
s=s.replace(needle,needle+' A separate exact finite-Frobenius countermodel blocks rigidity based only on numerical Euler data; an additive Hom invariant proves its class is different. For the singular diagonal-invariant quotient, the full derived self-correspondence has a nonzero Tor group in every positive degree and therefore leaves the bounded category.')
p.write_text(s)
q=r/'QUESTIONS.tsv'
with q.open(newline='') as f:rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for x in rows:
 if x['id']=='Q3-CENTRAL-POLYNOMIAL-HECKE':
  x['current_gate']+=' The actual finite coinvariant quotient has a bounded bifree scalar-complex countermodel with the same numerical Euler data but longest-object class, separated from the target by graded Hom; numerical-only formality fails. For S_tau=k[x²,xy,y²], Tor_i(A,A)=k in internal degree4+4i for every i≥1, so the full singular derived correspondence is unbounded.'
  x['approaches_tried']+='; finite-Frobenius bifree matrix construction and explicit extreme cohomology; graded Hom class separation; complete periodic singular-quotient resolution'
  x['next_step']='Retain the designated class and actual bounded central quadratic in the both-side nonflat case; neither numerical quotient rigidity nor the full singular derived correspondence supplies it.'
rows.append(dict(zip(fields,[
 'Q3-NONFLAT-QUOTIENT-ROUTES','F59 quotient continuation; EW§3.3–3.4 pp1105–1106; explicit periodic resolution',
 'Can numerical finite-Frobenius rigidity or the full singular derived correspondence close the remaining nonflat route?',
 'NUMERICAL_RIGIDITY_REFUTED_BY_EXPLICIT_DIFFERENT_CLASS_MODEL; FULL_SINGULAR_DERIVED_CORRESPONDENCE_PROVED_UNBOUNDED','F59',
 'For B=k[x,y]/(x²,y²), the actual normalized Z=L⊗_k L∨ shifted−2 satisfies a scalar-complex quadratic with coefficient Eulerδ² and Euler dimension16, but both extreme cohomologies are nonprojective. Its longest-object class is separated from the target by graded Hom. For A^tau=k[a,b,c]/(ac−b²), the explicit repeated matrixPhi gives Tor_i(A,A)=k<4+4i> for all i≥1. These results do not exclude every different bounded target-class polynomial-coefficient construction.',
 'Actual quotient normalization; homogeneous Frobenius pairing; explicit cohomology tables; associative Koszul chain isomorphism; additive Hom invariant; polynomial-lift exactness and full periodic Tor calculation',
 'Use the exact target class and relation maps in the remaining both-side nonflat problem; do not replace it by either failed route.'])))
with q.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
now=datetime.now(timezone.utc).isoformat()
with (r/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 w.writerow(['F59-QUOTIENT-ROOT',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','targeted proof check','Entire report and full fragment read/reconstructed: actual quadratic, both cohomology tables, graded Hom class distinction, complete periodic resolution and every Tor shift PASS. Final control-character and finding-environment deltas checked. No arithmetic purity inferred.',rep+' SHA256 '+rh+'; '+frag+' SHA256 '+fh])
 w.writerow(['F59-QUOTIENT-FRESH',now,'/root/gct_statements','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','independent re-proof','Whole report, source normalization and complete final-fragment match PASS.',rev+' SHA256 '+vh])
with (r/'ROOT_REVIEW_ITERATION_INVERSION_AND_CENTRAL_COEFFICIENTS.md').open('a') as f:
 f.write('\n## '+now+' — full quotient-route tests\n\nRoot read the entire report and entire generated fragment, reconstructed every extreme cohomology shift, the actual normalized chain quadratic and the graded-Hom class distinction, and checked the complete matrix resolution and all Tor shifts. The final report only repairs a control character; the final fragment uses the actual main finding environment and explicit F59 titles. Root also read the complete independent review. PASS at report'+rh+' and fragment'+fh+'. The finite-Frobenius example refutes only the numerical criterion; the full singular derived correspondence is unbounded, without an automatic arithmetic weight conclusion.\n')
with (r/'LEDGER.md').open('a') as f:f.write('\n## '+now+' — two nonflat routes tested exactly\n\nThe finite-Frobenius attempt cannot use numerical Euler data alone: a complete normalized bifree countermodel has nonprojective cohomology, and a graded-Hom invariant separates its class from the actual target. The full diagonal-invariant derived correspondence has Tor in every positive degree by an explicit periodic resolution and is unbounded. Both proofs and the separate dictionary are integrated after whole-proof/final-fragment checks. The remaining bounded target-class nonflat/nonflat problem is not declared solved.\n')
im=r/'IMPLICATIONS.md';im.write_text(im.read_text()+'\n## The nonflat quotient attempts\n\nF59 now records why two tempting continuations fail: nonzero numerical Euler data do not force projectivity over the finite coinvariant Frobenius algebra, and the full singular-invariant derived fiber product is unbounded. The explicit class-separating invariant and every positive Tor group are proved. A successful bounded polynomial-coefficient lift must retain the designated class and its actual relation, rather than appeal to either shortcut.\n')
print(json.dumps({'integrated':'F59-quotient-tests','questions':len(rows),'tex_sha256':sha(p),'utc':now},indent=2))
