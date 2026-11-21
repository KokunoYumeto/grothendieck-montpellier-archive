"""Integrate the bounded source audit and checked one-plus-three extension."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
r=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=r/'GCT_NSRH.tex'
assert sha(p)=='a781622bdf8269ab34562a0e788faddcb0aa7a8fd8e56ce070e5fd990d57cfd1'
items=[
 ('F65-INTEGRALITY','agent_viii_multiplication_integrality_audit.md','8cd13ba244efb01f85cf6ffdae50a935687c030522fd5900bc09c2849a091e9a','finding_F65_integrality_audit.tex','a2dcbce72c230034f0e3020584783c3d691fb4cfb9a5cf1d3eef42fbefe862f3','REVIEW_VIII_INTEGRALITY_THETA.md','3a63ed7d2c17f52fae2108e06122682f9631628292fe3003011bee771843e267','/root/rectangular_and_theta',r'\subsection{A normalization that cannot be a finite Frobenius trace}'),
 ('F67-ONE-THREE','agent_iterated_one_plus_three_tensor.md','49be681086d751416668de6b6ada1685376ec2336f9b4d7a15da5e6ddf9d6a04','finding_F67_one_plus_three.tex','134a39ae81ae17d6d70e16373ad9f3eef8e3b643c84f1dca6595ae0d3e05b13c','agent_F67_one_three_review.md','58a19c3e4953b4c5b7e7dd06e27fd27ef3bb7740138bcef2ebd223401437960c','/root/grothendieck_dictionary',r'\subsection{\fid{F64}: weight grading does not preserve the actual flag convolution}')]
s=p.read_text();da=r'\section{Archival audit and the Fable leads}\label{sec:archive}'
for fid,rep,rh,frag,fh,rev,vh,who,anchor in items:
 for name,h in [(rep,rh),(frag,fh),(rev,vh)]:assert sha(r/name)==h,name
 assert fh in (r/rev).read_text() and 'PASS' in (r/rev).read_text()
 body,dictionary=(r/frag).read_text().split('% Separate paragraph for Part III.',1)
 assert s.count(anchor)==1 and s.count(da)==1
 s=s.replace(anchor,body.rstrip()+'\n\n'+anchor)
 s=s.replace(da,dictionary.strip()+'\n\n'+da)
old='F67 gives a sharper iteration boundary: the actual whole tensor of two individually effective three-factor simples has a negative unmarked word coefficient, so strict effective iteration fails there without requiring an output projector.'
new='F67 gives a sharper iteration boundary: the actual whole tensors for one-plus-three and three-plus-three individually effective inputs have negative unmarked word coefficients. Strict effective iteration therefore fails for both specified outputs without requiring an output projector; the one-plus-three failure occurs at the same total factor count as the positive two-plus-two model.'
assert old in s;s=s.replace(old,new)
needle='These statements concern raw coefficients and leave normalized signed/factored positivity separate.'
assert needle in s
s=s.replace(needle,needle+' The bounded integrality audit finds no further obstruction in the six raw Figure~2 formulas: each has an actual mixed Tate scalar realization. The later rescaled and factored tables do not establish integrality of the omitted raw constants.')
p.write_text(s)
q=r/'QUESTIONS.tsv'
with q.open(newline='') as f:rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
byid={x['id']:x for x in rows}
extra=' The actual one-plus-three whole tensor also fails: its trace D²(D−2)²+(D²−8D+8)² has coefficients−4 at v^±6. This uses the ordinary first-factor simple and the same individually positive third-factor simple, with no output projector and the same explicit generic/specialization distinction. It is different from the positive two-plus-two output at total k4; no minimal-threshold claim is made.'
for qid in ['Q3-GCT','Q3-GRADED-COEFFICIENT-KERNELS','Q3-ITERATED-EFFECTIVE-SUMMANDS','Q3-ITERATED-WHOLE-TENSOR-COMPATIBILITY']:
 byid[qid]['current_gate']+=extra
x=byid['Q3-ITERATED-WHOLE-TENSOR-COMPATIBILITY'];x['state']='REFUTED_FOR_THE_ACTUAL_K1_PLUS_K3_AND_K3_PLUS_K3_WHOLE_TENSORS'
x['approaches_tried']+='; full unequal-input coproduct expansion and exact one-plus-three trace; separate mixed Tate witness'
byid['Q3-RAW-CANONICAL-PURITY']['current_gate']+=' The bounded F65 integrality audit adds no mixed-scalar obstruction: all six raw Figure2 formulas have integral Laurent coefficients and actual bounded mixed Tate witnesses. Rescaled/factored later vectors and coefficient-field traces/norms do not determine the omitted raw constants.'
rows.append(dict(zip(fields,[
 'Q3-PRINTED-RAW-INTEGRALITY','F65 bounded audit; VIII Conj2.7p15/3.4p24; Fig2p34; §5p27/5.1.2p29/5.4.1pp48–49; Figs24–35pp58–65',
 'Do the checked printed raw multiplication constants give a fractional-multiplicity obstruction to bounded mixed point traces?',
 'BOUNDED_AUDIT_COMPLETE_WITH_NO_COUNTEREXAMPLE; GROUPED_INTEGRALITY_CRITERION_AND_MIXED_WITNESSES_PROVED','F65',
 'All13 Figure2 labels reduce to six integral Laurent formulas; each admits an explicit bounded mixed Tate Euler realization under q_src=Q^n. Any finite uninserted Euler trace requires integer coefficients after equal arithmetic roots are grouped. The542 entries of the12 later tables are signed integers, but their rescaling/factor removal and field trace/norm roles do not recover the omitted raw constants. No global raw-integrality or absence theorem is claimed.',
 'Manual source-role and13-label matching; exact six-formula expansion and542-cell parsing; minimal-prime-denominator proof for exact vanishing-factor division; eventual Vandermonde; actual positive/negative-degree Tate construction',
 'The checked formulas supply no new denominator gate. An unprinted raw source counterexample would require its exact normalization and multiplication identity, while operation-compatible mixed geometry remains open.'])))
with q.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
now=datetime.now(timezone.utc).isoformat()
with (r/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for fid,rep,rh,frag,fh,rev,vh,who,anchor in items:
  w.writerow([fid+'-ROOT-FINAL',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','targeted proof check','Entire report and complete generated fragment read and reconstructed; all final source/proof deltas directly checked; separate dictionaries matched. PASS.',rep+' SHA256 '+rh+'; '+frag+' SHA256 '+fh])
  w.writerow([fid+'-FRESH-FINAL',now,who,'GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','independent re-proof','Whole-proof and complete final-text review PASS, including the exact limited source or specialization scope.',rev+' SHA256 '+vh])
 w.writerow(['VIII-INTEGRALITY-ROOT-CERTIFICATE',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','computation or formal certificate','Read and executed the exact script: six integral Laurent expansions and542 signed integer cells PASS. The13 formula-label coverage was checked manually against the source, not inferred from the script hard-coded formulas.','verify_viii_multiplication_integrality.py SHA256 6c786d8df3d10805fed48fb02844735a2e39c59ae864d9e4965795731dcea502'])
 w.writerow(['VIII-INTEGRALITY-ROOT-SOURCE',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','used and rechecked in this run','Read entire Figure2 source and matched every label/formula; freshly read original printedpp27,29,48–49. Corrected vector-convention and subsection-start locators retained. No unprinted constants or normalization exponents inferred.','VIII0709.0751v2; bounded audit exact source locators'])
with (r/'ROOT_REVIEW_ITERATION_INVERSION_AND_CENTRAL_COEFFICIENTS.md').open('a') as f:
 f.write('\n## '+now+' — bounded audit and one-plus-three final matches\n\n'
 'Root read the complete one-plus-three report and every line of its final fragment, reconstructed the unequal-input matrices, all product diagonals and both trace formulas, and read the complete independent review. The136/8 mixed Tate counts and generic/specialized scope check. Root did not claim a second execution of its exact script; author and fresh peer executed it. PASS at fragment134a39ae81ae17d6d70e16373ad9f3eef8e3b643c84f1dca6595ae0d3e05b13c.\n\n'
 'Root read the complete initial integrality fragment, then the final exact prime-denominator proof delta. This replaces the named Gauss-lemma invocation with the self-contained required Laurent argument. The corrected original printed locations are §5 vector conventionp27 and §5.2 startp29, with Figures3–5 stillpp35–37. Root freshly read those original pages andpp48–49, manually matched all13 Figure2 labels to the six formulas, read and executed the exact script and inspected its six full coefficient vectors. All assertions passed. The full final peer match is retained. This source audit is not main-gate movement.\n')
with (r/'LEDGER.md').open('a') as f:
 f.write('\n## '+now+' — smaller whole-output iteration test and bounded source audit integrated\n\n'
 'The full one-plus-three actual tensor already has a negative Laurent trace at total factor count4, alongside the distinct positive two-plus-two tensor at that same count. F67 retains both whole-output counterexamples, complete source occurrence and specialization boundaries, pure exclusions and actual mixed scalar witnesses. No minimal-threshold claim is made.\n\n'
 'The F65 bounded integrality audit is complete: its explicit grouped-integer criterion and six mixed Tate witnesses are proved, while the inspected raw formulas provide no fractional counterexample. Normalized later tables are not promoted into raw multiplication data. This unsuccessful denominator search is recorded and is not counted as movement.\n')
im=r/'IMPLICATIONS.md';t=im.read_text();t+='''\n## One-plus-three iteration and the bounded mixed-scalar audit\n\nF67's whole-output failure also occurs for the ordinary first-factor simple tensored with the individually effective third-factor simple. It does so at total factor count4, where a different two-plus-two output has the positive F66 model. This specifies which operation fails; it is not a minimality theorem or a statement about the full ambient ordinary tensor.\n\nF65's exact grouped-integrality condition is necessary even without purity, but the six printed raw multiplication formulas pass it and possess actual mixed Tate witnesses. The later printed vectors have omitted rescaling exponents and include coefficient-field traces and norms, so they cannot establish a global raw-integrality theorem. This bounded audit does not narrow the mixed-geometric gate.\n''';im.write_text(t)
print(json.dumps({'integrated':['F65-integrality','F67-one-plus-three'],'questions':len(rows),'tex_sha256':sha(p),'utc':now},indent=2))
