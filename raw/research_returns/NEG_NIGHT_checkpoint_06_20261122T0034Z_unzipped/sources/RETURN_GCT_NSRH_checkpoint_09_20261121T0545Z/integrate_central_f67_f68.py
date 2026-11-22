"""One-shot integration of three fully reviewed continuations."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

r=Path(__file__).resolve().parent
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
p=r/'GCT_NSRH.tex'
assert sha(p)=='6280dbe5c70c972b66259fd4d2c5bebc4c142e9ea0c383f894f2e62b2a5936a6'
items=[
 ('F59-CENTRAL','agent_soergel_central_coefficients.md','d276c3b9a8b85081eaab8e7cc7937e4cc4d3abc7c9a449a9137e4ae5301bef03',
  'finding_F59_central_coefficients.tex','69963bc08fc1d5c6385bcdc06f40a701ba1b8e2fc5d5a325d1e4d268551fdf3c',
  'agent_F59_central_coefficients_review.md','af343fd4fb98dc458762159edeab6997983343369ec7ea670833a0cc32ba5074','/root/grothendieck_dictionary',
  r'\subsection{Bounded kernels, finite-algebra characters, and an actual word relation}'),
 ('F67','agent_iterated_six_factor_tensor_gate.md','3c9dfc4388135ebe628d1c909568828fd0c74f886e13ef0cba95083f97be2354',
  'finding_F67.tex','8c2c2a116799ab94967ee610dabe92235966b3c925ec5fe2233812f08dbc8d4b',
  'agent_F67_six_factor_review.md','6bcb3f5353d8e5765ec6b215f04818c011773892393991b5aebf9a7288e35123','/root/grothendieck_dictionary',
  r'\subsection{\fid{F64}: weight grading does not preserve the actual flag convolution}'),
 ('F68','agent_tensor_inversion_gate.md','df472500e57cdd877f2ca7cf3dee320b0b3537a2792a05964060d04bd8f22551',
  'finding_F68.tex','5751824d8b300ab870f859a6fa15b6e265d68522807707d4f6c63c348b0e9e32',
  'REVIEW_TENSOR_INVERSION_GCT.md','de264b1251e266fa4ebb10cd8b0604d1e1a0afe947ee50c22397df050cf9ef1e','/root/gct_statements',
  r'\subsection{An effective-summand obstruction in the actual iterated three-strand family}'),
]
for fid,rep,rh,frag,fh,rev,vh,who,anchor in items:
 for name,h in [(rep,rh),(frag,fh),(rev,vh)]:assert sha(r/name)==h,name
 assert fh in (r/rev).read_text() and 'PASS' in (r/rev).read_text()
assert sha(r/'finding_F59_central_bib.tex')=='0714bea556c15ee85bc01dfc683c44fa3a69a8e34316468a9e1528ab7f8761c6'
# Check that each final heading delta is exactly the already-read fragment.
for name,new,old,oldhash in [
 ('finding_F67.tex',r"\paragraph{The \fid{F67} whole iterated tensor in Grothendieck's language.}",r"\paragraph{The whole iterated tensor in Grothendieck's language.}",'e8d43cc3ba42c0f1fff5fe2a4389f0c70bb3fef88d631ae5fc124800866cb619'),
 ('finding_F68.tex',r'\paragraph{The \fid{F68} distinction between actual duality and virtual inversion.}',r'\paragraph{Actual duality versus virtual inversion.}','d77c5d1610a7848195b5fee1b730b444b016d00ccce7e59c22269f5503d69c72'),
 ('finding_F59_central_coefficients.tex',r"\paragraph{The F59 central polynomial coefficients in Grothendieck's language.}",r"\paragraph{Central polynomial coefficients in Grothendieck's language.}",'80844da4418c9d0fe2f6e16e81258cb37eec0e31fc570efed112a7321fad54bf'),
]:
 original=(r/name).read_text().replace(new,old)
 assert hashlib.sha256(original.encode()).hexdigest()==oldhash,name+' has an unreviewed delta'
s=p.read_text()
da=r'\section{Archival audit and the Fable leads}\label{sec:archive}'
for fid,rep,rh,frag,fh,rev,vh,who,anchor in items:
 body,dictionary=(r/frag).read_text().split('% Separate paragraph for Part III.',1)
 assert s.count(anchor)==1 and s.count(da)==1
 s=s.replace(anchor,body.rstrip()+'\n\n'+anchor)
 s=s.replace(da,dictionary.strip()+'\n\n'+da)
s=s.replace('findings A01 and F01--F66,','findings A01 and F01--F68,')
s=s.replace(r'\end{thebibliography}',(r/'finding_F59_central_bib.tex').read_text().rstrip()+'\n'+r'\end{thebibliography}')
old='The changed-scalar ordinary-Hecke route is now closed by F59, rather than left at a nonflat-cohomology gate. Polynomial-differential coefficient bimodules, unbounded objects and different convolution categories remain different premises and are not covered by the scalar theorem.'
new=r'''The changed-scalar ordinary-Hecke route is closed by F59. Its polynomial-coefficient extension proves that a perfect diagonal coefficient cannot repair the designated quadratic if either its own cohomology or the generator cohomology is flat. Invariant descent supplies actual central maps, while a single root-Koszul coefficient fails to commute with the ramified reflection correspondence unless its polynomial is invariant. A remaining bounded polynomial-coefficient construction must have nonflat cohomology on both sides, the designated generator class and actual quadratic and centrality maps. An explicit different-class example shows that central non-scalar quadratics do exist; it is not the required lift.'''
assert old in s;s=s.replace(old,new)
needle='F64 proves that canonical weight grading and perverse or ordinary cohomology splitting fail to preserve this convolution.'
assert needle in s
s=s.replace(needle, r'F68 further excludes tensor-inverting the actual torus or projective-line coefficient through any additive strong monoidal functor into a nonzero target, even an unbounded nonsymmetric one. The relative nonsplit coefficient is covered by its actual dual pair and zero source trace. Formal ring inversion and geometric quotient operations remain distinct. '+needle)
needle='These are distinct, explicitly delimited conclusions.'
assert needle in s
s=s.replace(needle,r'F67 gives a sharper iteration boundary: the actual whole tensor of two individually effective three-factor simples has a negative unmarked word coefficient, so strict effective iteration fails there without requiring an output projector. The occurrence is generic; its chosen input lattice is not identified with an ambient direct summand at the collision. A mixed Tate scalar witness survives. These are distinct, explicitly delimited conclusions.')
s=s.replace('These results still permit triangle-only relations, nontrivial coefficient complexes, and geometric convolution without a matrix-cohomology character functor.',
            'The F60 obstruction still permits triangle-only relations, nontrivial coefficient complexes and geometric convolution without a matrix-cohomology character functor; the separate F59 theorem excludes its own full bounded scalar route.')
p.write_text(s)

q=r/'QUESTIONS.tsv'
with q.open(newline='') as f:rd=csv.DictReader(f,delimiter='\t');fields=rd.fieldnames;rows=list(rd)
byid={x['id']:x for x in rows}
poly=' Perfect diagonal coefficients with polynomial differentials also fail if either all H(C) or all H(X) are flat. Any remaining such target requires nonflat cohomology on both sides and actual centrality/quadratic maps; invariant descent supplies genuine central structures but the constructed example has a different generator Euler class.'
for qid in ['Q3-BOUNDED-ORDINARY-HECKE','Q3-ALTERED-SCALAR-HECKE']:
 byid[qid]['current_gate']+=poly
 byid[qid]['next_step']='The scalar route is closed. The distinct perfect diagonal-coefficient route requires both cohomologies nonflat, the exact target class, and actual centrality and quadratic maps.'
byid['Q3-GCT']['finding_ids']+=',F67,F68'
byid['Q3-GCT']['current_gate']+=poly+(' F67 excludes strict effective actual iteration on the whole k3+k3 tensor of an individually positive input, without an output projector. F68 excludes normalization by tensor-inverting the actual torus/P1 object under every nonzero additive strong monoidal target retaining the stated source data. Actual geometric quotients and filtered or mixed operations remain distinct possibilities.')
byid['Q3-GCT']['approaches_tried']+='; invariant polynomial centrality; both-side nonflat gate; whole k3+k3 restriction; universal additive monoidal inversion'
byid['Q3-GCT']['next_step']='Construct and test genuine geometric quotient or filtered normalized-factor operations with composition coherence and designated labels; attack the both-side nonflat perfect-coefficient target. Independent local/dual bounds remain required.'
byid['Q2']['finding_ids']+=',F67,F68'
byid['Q2']['current_gate']+=(' The central perfect-coefficient alternative must be nonflat on both sides. Whole k3+k3 actual iteration fails strict effective kernels even without an output projector. Additive strong monoidal inversion of the actual torus/projective-line coefficients is excluded in every nonzero target; geometric quotient normalization is a separate candidate.')
x=byid['Q3-TENSOR-INVERSE'];x['finding_ids']='F38,F62,F68'
x['state']='REFUTED_FOR_EVERY_NONZERO_ADDITIVE_STRONG_MONOIDAL_TARGET_WITH_THE_STATED_SOURCE_DATA'
x['source_and_locator']+='; F68; Milne16.1/16.2,22.1/22.3,23.2,24.1/24.2'
x['current_gate']=('A finite sum of at least two invertible objects cannot become invertible under an additive strong monoidal functor to a nonzero additive monoidal category. The actual derived Weil torus and P1 objects have such splittings. A separate zero-source-trace lemma transports the actual dual pair and source symmetry as maps, without requiring target symmetry; it excludes the relative nonsplit F62 coefficient and its stated zero-trace normalizations. Unbounded and nonfaithful targets do not evade these conclusions. Formal Grothendieck/trace-ring inverses and geometric quotients are not object inverses.')
x['approaches_tried']+='; invertible unit-summand lemma; transported dual-pair adjunction; actual rational-point splitting and smooth duality; relative local perfectness and zero source trace'
x['next_step']='This tensor-inversion route is closed under the stated functor premises. Test a geometric quotient or a different extraction operation without claiming it is such an inverse.'
x=byid['Q3-NONPROPER-FACTOR-OPERATIONS'];x['finding_ids']+=',F68'
x['current_gate']+=' F68 excludes tensor inversion of the actual relative coefficient in every nonzero additive strong monoidal target retaining its dual pair and source symmetry, without any global splitting or target boundedness assumption.'
x['next_step']='Construct a genuine relative geometric quotient/factor extraction, then prove its composition coherence and exact designated source comparison.'
for qid in ['Q3-ITERATED-EFFECTIVE-SUMMANDS','Q3-GRADED-COEFFICIENT-KERNELS']:
 x=byid[qid];x['finding_ids']+=',F67'
 x['current_gate']+=' F67 shows that whole-tensor models do not repair unrestricted actual iteration: the entire k3+k3 tensor of the individually effective k3 simple has negative coefficients at v^±10 in its unmarked two-word trace. No output projector is needed. The tested constituent is generic and its chosen lattice has the explicit specialization limitation.'
 x['next_step']='Use a mixed/signed operation, a restricted input category, or a different operator/source comparison. Whole k2+k2 positivity alone cannot supply unrestricted effective iteration.'
byid['Q3-WHOLE-ITERATED-POSITIVE-TENSOR']['next_step']='This k2+k2 construction is complete in its stated scope. F67 blocks extension to the tested k3+k3 whole tensor; compare mixed/signed iteration and source labels.'
for key in ['finding_ids','current_gate']:byid['Q6'][key]=byid['Q6'][key].replace('F01–F66','F01–F68')
newrows=[
 ['Q3-CENTRAL-POLYNOMIAL-HECKE','F59 polynomial continuation; EGAI1.3.7/1.4.1; Stacks00NX',
  'Can a genuinely central perfect diagonal coefficient with polynomial differentials repair the designated ordinary-Hecke quadratic?',
  'OPEN; CENTRALITY_AND_BOTH_SIDE_NONFLAT_NECESSITY_PROVED','F59',
  'A single nonzero homogeneous Koszul polynomial commutes with an actual reflection generator iff it is reflection invariant. Invariant-descended complexes have coherent actual central maps. The designated quadratic fails if either coefficient or generator cohomology is flat. The remaining case has nonflat cohomology on both sides; an extra torsion top can disappear generically. A constructed central non-scalar quadratic has coefficient Eulerδ² but generator class b1b2, not P.',
  'Principal annihilator ideals; ramified versus graph restrictions; invariant pullback and Koszul coherence; one-sided Kunneth and projective summands; explicit different-class Koszul example',
  'Retain the exact target class while testing the both-side nonflat case; analyze coinvariant and singular-correspondence approaches without importing the regular scalar theorem.'],
 ['Q3-ITERATED-WHOLE-TENSOR-COMPATIBILITY','F67; Blasiak1010.0421v2 Def2.5/Eq11/13/24/25/26,Thm3.4/Cor3.5',
  'Can the actual iteration of individually effective inputs retain strict effective kernels on the whole tested output?',
  'REFUTED_FOR_THE_ACTUAL_K3_PLUS_K3_TENSOR','F67',
  'The actual k3 simple has positive two-state named matrices and quadratic kernels. Its whole four-dimensional k3+k3 restriction has unmarked trace D^6+(-D³+18D²−48D+32)², with Laurent coefficients−12 at±10. This excludes all simultaneous effective named bases and the specified effective kernel iteration without an output projector. The pure point comparison fails; a bounded mixed Tate scalar witness exists. Generic ambient occurrence does not imply a regular ambient specialization lattice.',
  'Exact coproduct matrices; all product diagonals; source occurrence; explicit failed specialization relation; Laurent cone and pure-point criteria; mixed Tate witness',
  'A compatible iteration must change the effective, admissible-input, operator, or trace comparison premise and identify the designated source operations.']]
rows.extend(dict(zip(fields,row)) for row in newrows)
assert len({x['id'] for x in rows})==len(rows)
with q.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

now=datetime.now(timezone.utc).isoformat()
with (r/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for fid,rep,rh,frag,fh,rev,vh,who,anchor in items:
  w.writerow([fid+'-ROOT-COMPLETE',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','targeted proof check','Entire report and complete final fragment read and reconstructed; final dictionary-heading deltas matched; exact assumptions and separate dictionaries retained. PASS.',rep+' SHA256 '+rh+'; '+frag+' SHA256 '+fh+'; ROOT_REVIEW_ITERATION_INVERSION_AND_CENTRAL_COEFFICIENTS.md'])
  w.writerow([fid+'-FRESH-COMPLETE',now,who,'GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','independent re-proof','Whole proof, specified primary-source contexts and every final-fragment line independently checked; PASS with recorded exact scope.',rev+' SHA256 '+vh])
 w.writerow(['F67-ROOT-EXACT-CERTIFICATE',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','computation or formal certificate','Read and executed the exact SymPy certificate; both full coproduct matrices, quadratics, all product diagonals, Laurent coefficients, multiplicity totals and specialization identity PASS. No proof-assistant verification.','verify_iterated_six_factor_tensor.py SHA256 b84cea81e62efef36c6d7dd3cdd60394cd2bb16989ed4044bd9646f021c8357b'])
 w.writerow(['STACKS-00NX-ROOT',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','used and rechecked in this run','Fresh primary full statement and proof read; parts1–3 give exactly finite presented flat, finite projective and finite free direct summand equivalence.','https://stacks.math.columbia.edu/tag/00NX; Lemma10.78.2'])
 w.writerow(['BLASIAK-F67-ROOT-SOURCE',now,'/root','GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121','used and rechecked in this run','Fresh original PDF extracted-text contexts read on pp6–9,11–13; exact actual inclusion, matrix convention, k3 simple, occurrence and specialization caveat matched. Known results are inputs.','Blasiak1010.0421v2 Def2.5,Eq8–17/24–26,Thm3.4,Cor3.5'])
with (r/'ROOT_REVIEW_ITERATION_INVERSION_AND_CENTRAL_COEFFICIENTS.md').open('a') as f:
 f.write('\n## '+now+' — final integration match\n\nRoot read the complete independent final reviews for all three additions. Every line of the F67 fragment was read after the report; its added numerical-positivity clarification is correct. The final F59, F67 and F68 dictionary-heading changes only add their explicit finding IDs; no proof changed. All final hashes were checked at integration.\n\n'+ '\n'.join('- '+fid+': '+frag+' SHA256 '+fh for fid,rep,rh,frag,fh,rev,vh,who,anchor in items)+'\n')
with (r/'LEDGER.md').open('a') as f:
 f.write('\n## '+now+' — central polynomial boundary, whole iteration and universal inversion\n\n'
 'F59 now narrows the separate perfect diagonal-coefficient alternative to nonflat cohomology on both sides, with actual centrality and the designated generator class still required. It proves invariant descent and a precise single-polynomial centrality test, and supplies a different-class non-scalar example so the exclusion is not overextended.\n\n'
 'F67 excludes unrestricted strict effective actual iteration on a specified whole tensor of individually positive inputs, without requiring an output projector. F68 closes tensor inversion of the actual torus/P1 coefficients under every nonzero additive strong monoidal target retaining the stated finite source data, including unbounded nonsymmetric targets. These strictly narrow preexisting main realization gates. Full proofs and separate dictionaries are integrated after root and independent whole-proof/final-fragment checks.\n\n'
 'The bounded VIII integrality search found no new denominator obstruction in its explicitly checked printed formulas; it is not counted as movement. Active follow-up tests actual geometric quotient normalization and the remaining both-side nonflat target. Next scheduled review05 remains06:00UTC and checkpoint09 remains05:45UTC.\n')
im=r/'IMPLICATIONS.md';t=im.read_text().replace('integrates findings F01–F66','integrates findings F01–F68')
t=t.replace('The first scheduled three-hour review occurred at02:00UTC with mathematical movement; the no-movement count is0 and the next review is03:00UTC.',
            'The dated hourly reviews and current stop-rule count are recorded in REVIEW_STATE.json and the PROGRESS_REVIEW files; this synthesis does not advance that schedule.')
t+='''\n## Actual operations beyond scalar coefficients\n\nF59's perfect diagonal-coefficient extension excludes the desired quadratic if either cohomology side is flat. A single Koszul polynomial must be reflection invariant to commute with the actual ramified generator, while invariant descent does supply coherent central maps. The exact remaining bounded coefficient case is nonflat on both sides and must retain the designated Euler class. The explicit central different-class example shows why mere existence of polynomial-coefficient quadratics does not solve it.\n\nF67 closes an additional preexisting iteration alternative: even omitting an effective projector in the output does not make unrestricted effective iteration possible on all individually positive inputs. The actual k3+k3 whole tensor has a negative Laurent word coefficient. Its generic occurrence and its failed ambient specialization lattice are stated separately. A mixed scalar trace witness remains and does not give the required operations.\n\nF68 removes target boundedness, symmetry and faithfulness as escapes from actual coefficient inversion. The unit-summand lemma uses actual biproduct data; the relative zero-trace lemma retains duality and the source symmetry map without splitting the Chern extension. These are categorical restrictions, not prohibitions on formal K0 localization or actual geometric quotients. The latter must be constructed with their own composition maps and designated comparison. The separate PartIII paragraphs give exact Grothendieck framework and archive anchors for every statement.\n'''
im.write_text(t)
(r/'STATUS_TIME.txt').write_text('WORK IN PROGRESS\nSnapshot UTC: '+now+'\nTeX integrates F01–F68, including all bounded-scalar and central-polynomial F59 continuations.\nPDF remains the verified checkpoint08 version until the checkpoint09 rebuild.\nNext checkpoint09:05:45UTC. Next scheduled review05:06:00UTC. Consecutive no-movement count:0.\nActive gates: actual geometric quotient/composition, both-side nonflat perfect coefficients, mixed/filtered designated labels and independent spectral bounds.\n')
print(json.dumps({'integrated':['F59-central','F67','F68'],'questions':len(rows),'tex_sha256':sha(p),'utc':now},indent=2))
