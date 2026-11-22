"""Integrate only the frozen whole-reviewed F59 scalar extension and F62."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib
r=Path(__file__).resolve().parent
entries=[
('agent_soergel_scalar_complex_gate.md','f0805ab3ae6735815c3acd08b4b42272e6d53a1308cdabb0d2016734278ceafb'),
('finding_F59_scalar_complex.tex','d2582ec9bd1d71877eb2bb0546abc380a71e257aa686e125164556ec6eb68fa7'),
('REVIEW_SOERGEL_SCALAR_COMPLEX_THETA.md','74b54fdc5257c981a4bad130d355ae6ff59153aee30c9acc22cfe716f6304f6d'),
('agent_nonproper_torus_kernel.md','b70ed1e87088267222e206f1e1fec8147f288f816846462f5d495b902f87398a'),
('finding_F62.tex','6fd83439f9c710c3a34d8bd052a429367ed0bf0b0b38facc0605eb247c151ec8'),
('agent_F62_nonproper_kernel_review.md','99d91af7ed3db4f5ee9a64841033e8b5a40bf709ea479910751d6d17541c5d44')]
for name,sha in entries: assert hashlib.sha256((r/name).read_bytes()).hexdigest()==sha,(name,'changed')
assert entries[1][1] in (r/entries[2][0]).read_text()
assert entries[4][1] in (r/entries[5][0]).read_text()
p=r/'GCT_NSRH.tex'; s=p.read_text(); assert r'\label{f:alteredScalarSoergel}' not in s and r'\label{f:nonpropertorus}' not in s
for name,needle in [
('finding_F59_scalar_complex.tex',r'\subsection{Bounded kernels, finite-algebra characters, and an actual word relation}'),
('finding_F62.tex',r'\subsection{A normalization that cannot be a finite Frobenius trace}')]:
 body,dictionary=(r/name).read_text().split('% Separate paragraph for Part III.',1)
 assert s.count(needle)==1; s=s.replace(needle,body.rstrip()+'\n\n'+needle)
 anchor=r'\section{Archival audit and the Fable leads}\label{sec:archive}'
 assert s.count(anchor)==1; s=s.replace(anchor,dictionary.strip()+'\n\n'+anchor)
s=s.replace('findings A01 and F01--F61,','findings A01 and F01--F62,')
needle='A compatible realization of those signed/factored operations, a source-prescribed higher categorical presentation and designated simple/global labels remain.'
assert needle in s
s=s.replace(needle,'With an altered bounded scalar coefficient, F59 now forces uniform generic cohomology on the identity and diagonal-reflection graphs and excludes every lift with flat cohomology. F62 constructs actual standard nonproper flag convolution and the exact torus factors in two printed source constants. Its nonzero Chern-class boundary obstructs replacing the relative coefficient by a constant fiber complex; neither equality of all fiber traces nor formal division supplies the missing operation. '+needle)
# Break the existing dense Part IV discussion at substantive transitions; no mathematical edits.
start=s.index(r'\section{What a sufficient nonstandard package would have to contain}')
end=s.index(r'\section{Approaches attempted and their exact outcomes}',start)
seg=s[start:end]
for phrase in ['F48 supplies an actual all-degree','F50 supplies the normalized','F53 supplies coherent geometric','F54 removes the integral-weight','F55 constructs an actual fractional','F56 now constructs the rank-three','F57 excludes extending','F58 also excludes','F59 excludes every bounded','F60 excludes bounded','F61 supplies a coherent','With an altered bounded scalar']:
 seg=seg.replace(' '+phrase,'\n\n'+phrase)
s=s[:start]+seg+s[end:];p.write_text(s)
q=r/'QUESTIONS.tsv'
with q.open(newline='') as f: rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
for x in rows:
 if x['id']=='Q3-GCT':
  x['finding_ids']+=',F62';x['current_gate']+=' Altered scalar coefficients still require nonflat cohomology in the ordinary-Hecke lift. Actual standard nonproper convolution produces the source torus factors, but its nonzero relative Chern extension excludes a constant coefficient replacement; designated nonstandard relation maps and normalized extraction remain.'
  x['next_step']='Test a nonfactorable nonflat ordinary-Hecke complex with altered scalar coefficient, or construct relative signed-factor extraction preserving actual geometric maps and the designated labels; prove independent weight estimates.'
 if x['id']=='Q3-BOUNDED-ORDINARY-HECKE':
  x['current_gate']+=' If the coefficient is changed to a bounded scalar k-complex with the same Euler class, generic cohomology must be uniform on {e,tau} degreewise; all-flat cohomology is still impossible. The two explicit dot/Rouquier candidates cannot be repaired by any such scalar complex.'
  x['next_step']='The changed-scalar case now requires nonflat cohomology and actual quadratic maps; polynomial-differential coefficient bimodules and other categories remain separate premises.'
 if x['id']=='Q3-PURE-POINT-COMPLEX':
  x['finding_ids']+=',F62';x['current_gate']+=' F62 supplies actual standard convolution maps for the nonproper alternative and proves the relative torus coefficient is not the constant fiber complex.'
 if x['id']=='Q6':x['current_gate']=x['current_gate'].replace('F01–F61','F01–F62')
new=[
['Q3-ALTERED-SCALAR-HECKE','F59 scalar continuation; EWLocalized1.1/Thm1.6; SGA6I4.7–4.8','Can a bounded scalar complex repair the actual ordinary-Hecke quadratic?','UNIFORM_GENERIC_SUPPORT_PROVED; FLAT_COHOMOLOGY_AND_TWO_CANDIDATES_REFUTED','F59','Actual quadratic implies generic H(X)=d(u)(e+tau)/2, so every ungraded cohomological coefficient of C is even. Full internal grading is not retained under localization. If every H^j(X) is flat, global graph splitting restores grading and forces d(v,u)=2a(v,u), contradicting the odd outer Euler coefficients of delta². Nonflat cohomology remains open.','Positive idempotent finite-group measure; Euler support; codimension-two graph splitting; canonical Kunneth; scalar candidate tests; exact finite-fiber amplitude boundary','Investigate genuinely nonflat cohomology with actual relation maps, not a generic Euler-class construction.'],
['Q3-NONPROPER-FACTOR-OPERATIONS','F62; IV Example19.3 Fig21; VIII Fig2; Milne16.1/17.10/18.4/22.5/23.2–3','Can actual nonproper ambient operations produce the source vanishing factors, and can they be treated as constant scalar coefficients?','ACTUAL_STANDARD_OPERATIONS_PROVED; CONSTANT_COEFFICIENT_SPLITTING_REFUTED','F62','For H=j!E on distinct P1 pairs, the square has an actual nonsplit localization triangle. The off-diagonal coefficient is the compact pushforward of O(1,-1)^times, with nonzero Chern boundary. It has all fiber traces Q−1 but differs from the constant fiber complex. Two factors give IV c0 and a shifted/twisted P2 factor gives the exact VIII printed coefficient. Neither canonical-label identification nor a nonstandard quadratic is inferred.','Actual path correspondences; graph-of-map torsor; Gysin sequence; projective-bundle restriction matrix; global dimensions2vs4 and4vs8; finite tensor-inverse obstruction','Construct a functorial relative factorization or extraction retaining the Chern maps and source specialization, with a designated canonical comparison.']]
for row in new:rows.append(dict(zip(fields,row)))
assert len({x['id'] for x in rows})==len(rows)
with q.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
now=datetime.now(timezone.utc).isoformat()
with (r/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for ident,who,typ,outcome,inds in [
 ('F59-SCALAR-COMPLETE','/root','targeted proof check','Entire report and complete final fragment read and reconstructed; generic positive support, lost grading warning, global flat graph split, canonical Kunneth, odd coefficient contradiction and exact residual scope PASS.',[0,1]),
 ('F59-SCALAR-FRESH','/root/rectangular_and_theta','independent re-proof','Whole report and every final-fragment line checked; PASS with scalar k-complex and homotopy-quotient scopes.',[2]),
 ('F62-COMPLETE','/root','targeted proof check','Entire original report and final outer-nonsplitting delta read; complete final fragment matched. Actual correspondences, torsor orientation, Chern map, all cohomology and dimension calculations, source trace normalizations and finite inverse scope PASS.',[3,4]),
 ('F62-FRESH','/root/grothendieck_dictionary','independent re-proof','Whole report/fragment plus outer-triangle delta reconstructed; original Milne and source coefficient contexts rechecked; PASS.',[5])]:
  w.writerow([ident,now,who,'GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121',typ,outcome,'; '.join(entries[j][0]+' SHA256 '+entries[j][1] for j in inds)])
with (r/'LEDGER.md').open('a') as f:f.write('\n## '+now+' — altered scalar gate and actual nonproper operations integrated\n\nFull reviewed F59 scalar continuation narrows the changed-coefficient route to nonflat cohomology; both original explicit candidates still fail. F62 constructs actual standard flag convolution and source scalar-factor witnesses, proving the relative coefficient has a nonzero Chern-class extension and cannot be replaced by its constant fiber complex. All new proof text and separate dictionaries have whole checks. These do not identify the unknown nonstandard canonical labels. The192-page checkpoint07 PDF remains the previous verified build until the next rebuild.\n')
im=r/'IMPLICATIONS.md';t=im.read_text().replace('The paper integrates findings F01–F54','The paper integrates findings F01–F62')
t+='\n## Altered scalar coefficients and nonproper operations\n\nF59 now permits an arbitrary bounded scalar k-complex in the tested quadratic and proves that any surviving lift must have nonflat cohomology. Generic localization forces equal identity/diagonal-reflection multiplicities in every cohomological degree; an actual globally flat lift restores the full grading and contradicts integral parity. This is a narrower residual question, not an exclusion of all derived geometry.\n\nF62 supplies actual ambient convolution, localization maps and the nonproper torus factors occurring in IV and VIII. The relative compact coefficient is not constant: its Chern class is a nonzero connecting morphism, and ordinary base cohomology detects the difference even though every fiber trace agrees. A torus factor cannot be inverted as a finite derived coefficient object. Thus normalized positivity needs an actual relative extraction or filtration and canonical-label comparison. A pointwise polynomial factorization alone cannot supply either. The separate dictionary uses the same exact EGA, SGA3/5/6 and cote90/17,133/18 anchors, with the explicit Chern calculation in the six-operation framework.\n';im.write_text(t)
readme=r/'README.md';t=readme.read_text().replace('integrates F01–F61','integrates F01–F62');t+='\nThe TeX now also contains the altered-scalar F59 continuation and F62 actual nonproper flag operations. The current PDF remains the verified checkpoint07 build throughF61 pending the next rebuild. See STATUS_TIME.txt for the precise build state.\n';readme.write_text(t)
(r/'STATUS_TIME.txt').write_text('WORK IN PROGRESS\nSnapshot UTC: '+now+'\nTeX integrates F01–F62, including altered-scalar continuation; PDF remains verified192-page checkpoint07 throughF61 until next rebuild.\nReview03 movement yes, count0. Next review and checkpoint08 due05:00UTC.\nMain residual gates: nonflat altered-scalar lift, actual relative normalized extraction and canonical labels, independent local/dual estimates.\n')
print('Integrated F59 scalar and F62;',len(rows),'question rows;',hashlib.sha256(p.read_bytes()).hexdigest())
