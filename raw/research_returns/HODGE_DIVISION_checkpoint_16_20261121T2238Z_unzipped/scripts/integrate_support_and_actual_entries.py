"""Integrate E829/E830 after complete author, root and peer readings."""
from pathlib import Path
from datetime import datetime, timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
proofs={'E829':'agents/sixfolds/rm_surface_support_wedge_gate_section.tex','E830':'agents/sixfolds/rm_actual_elliptic_coupling_gate_section.tex'}
hs={'E829':'f9cc55075bde5e099ec695c4ddd309f6095f71933ad52eb795c2393bca361f8f','E830':'6c1761d5c46dadcd28482ceceed88b9a7e1fd748002bed11e04982b4cfa40d28'}
for k,p in proofs.items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==hs[k]
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert all(r['id'] not in ('Q5ac','Q5ad') for r in rows)
(R/'research/gates_before_support_actual_entries.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q5i'},indent=2)+'\n')
p=R/'HODGE_DIVISION.tex';s=p.read_text();anchor=r'\input{agents/sixfolds/rm_equal_hull_equivariance_section.tex}'
s=change(s,anchor,anchor+'\n'+'\n'.join(r'\input{'+v+'}' for v in proofs.values()))
s=change(s,'outside this statement.\nRank-deficient unit matrices,',r'''outside this statement.
SF-E829 treats every nonzero cross-line difference of Hermitian rank
at least two. Only rank-two index-one surface directions contribute
exceptional product lines. If their span is $Z\subset\Lambda^2H^1(O_X)$,
then $w=6-\dim Z-\dim\operatorname{rad}(q_\wedge|_Z)$ diagonal
classes survive per selected block; the actual invariant middle Ext
is at least $w(u+|J|)$. The product-isogeny and all cup-product cases
are proved. Nonacyclic elliptic directions are outside that common
annihilator theorem.
SF-E830 then follows the actual extension-matrix entries through both
triangle boundaries. Its entry-specific support $Z_e$ obeys the same
wedge formula and includes elliptic differences. Along one positive
elliptic direction, actual coefficient rank $r_e$ leaves $6-2r_e$
classes per selected block. Ten or more selected blocks require
$r_e=3$; five through nine require $r_e\ge2$. The constructed
full-rank indecomposable elliptic extension has pure exponential
character and is explicitly not a balanced seed. These are necessary
support and rank conditions, with the actual filtration, action and
selected unit-block vanishings retained.
Rank-deficient unit matrices,''');p.write_text(s)
g829=('SF-E829 extends the diagonal obstruction to arbitrary nonzero divisor differences of Hermitianrank>=2 and acyclic rank1 pairs. Only surface-index1rank2 pairs contribute support lines; their spanZ inLambda2H1O gives w=6-dimZ-dimrad(qwedge|Z), hence ext2Gamma>=w(u+|J|). Rank3 and rank2index0/2 are harmless. Single or two complementary surface supports givew4; two intersecting supports givew2. Nonacyclic elliptic directions remain outside this whole-Ext version. ')
g830=('SF-E830 replaces whole-Ext hypotheses by actual extension-entry spans, including all positive numerical ranks and trivial/flat differences. Its actual supportZe gives ext2Gamma>=(6-dimZe-dimrad)(u+|J|). For one positive elliptic direction, coefficientrankr leaves6-2r classes per block; >=10selectedblocks requiresr3,5-9requiresr>=2,4requiresnonzero. The actual indecomposable full-rank elliptic example has pure exponential character and is not a balanced seed. ')
for r in rows:
 if r['id']=='Q5i':r['finding_ids_or_current_gate']=change(r['finding_ids_or_current_gate'],'Remaining: unstable bundles',g829+g830+'Remaining: unstable bundles').replace('outsideE818/E821/E822/E823/E824/E825/E826/E827/E828','outsideE818/E821/E822/E823/E824/E825/E826/E827/E828/E829/E830')
rows.extend(dict(zip(fields,x)) for x in [
 ['Q5ac','Prompt target5; arbitrary surface support directions','Can an actual two-slope balanced seed violate the wedge-survivor cap for arbitrary nonacyclic rank-at-least-two cross differences?','refuted',g829+'Complete root/peer proof and actual cup/LES reviews PASS.'],
 ['Q5ad','Prompt target5; actual elliptic extension coefficients','Can an actual balanced extension evade the diagonal obstruction with insufficient actual elliptic coefficient rank under the stated block-count hypotheses?','refuted',g830+'Complete root/peer proof and actual triangle reviews PASS; no sufficiency or generic-rank assumption.']])
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('SF-E829','targeted proof check','Root read all292draft lines at4cab77bf and all308canonical lines atf9cc5507, plus full conversion record. PASS rational selfadjoint Riemann-form complement, lattice isogeny, actual line factorization, finite trace, exhaustive rank/index cup products, wedge-radical complement and actual invariant E827 boundaries. Two H-star Markdown expressions made inline math; no theorem change.',proofs['E829']),
 ('SF-E830','targeted proof check','Root read all291draft lines atdbe5e856 and all308canonical lines at6c1761d5, plus full conversion record. PASS actual-entry-only outgoing boundaries, full matrix incoming products, selected B trace, all rank/trivial/flat support cases, rank thresholds and genuine indecomposable elliptic bundle with pure character. No constructed finite action or semiregularity asserted for example.',proofs['E830']),
 ('SF-E829/E830 independent audit','independent re-proof','G34 independently read both full proofs, reread E827 maps, and reconstructed cup/exterior conditions; both PASS. Root read both entire audit reports and the entire separately authored exact exterior checker. Actual certificate PASS0.032552646s for12rank/index cases, wedge radicals, ellipticrank0-3, trivialspans0-4, thresholds4-30. No author program imported; no geometry certified by computation.','agents/g34_eightfolds/bireflection/SURFACE_SUPPORT_WEDGE_PEER_AUDIT.md; agents/g34_eightfolds/bireflection/ACTUAL_ELLIPTIC_COUPLING_PEER_AUDIT.md; agents/g34_eightfolds/bireflection/audit_surface_elliptic_gates.py'),
 ('SF-E829/E830 cohomology and supplied-source boundary','used and rechecked in this run','Mumford original index/Riemann-Roch pp150-153 and Hermitian index pp162-163 retain complete earlier root readings; peer freshly reread original statements and rendered162-163. Pic0 vanishing has direct proof in draft. Full supplied S21/published BF statuses remain unchanged. No Markman/Severn/032 promotion.','agents/sixfolds/SOURCE_LOG.md; '+proofs['E829']+'; '+proofs['E830'])]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Arbitrary surface directions and actual elliptic coefficient gates\n\n'+now+' — Q5ac/Q5ad refuted and Q5i strictly reduced. '+g829+g830+'The overlapping results are successive strengthening of one diagonal mechanism, not independent balanced-seed constructions. Both full proofs and canonical conversions were read by root and peer; the actual example is a method boundary, not movement. This is not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Actual divisor supports narrow the balanced-RM alternative\n\n'+g829+g830+'The necessary obstruction concerns actual coherent objects under the specified finite translation/tensor action. It neither pulls semiregularity along an isogeny nor substitutes irrational RM embedding planes for abelian subvarieties. The condition-A supplier gate, cote16 scan050, is narrower. EGA/SGA and realization placement, condition-I positivity, Cayley-Hamilton division, and motivic/L-function limits remain as recorded in the common framework.\n')
p=R/'research/frameworks.tex';p.write_text(change(p.read_text(),'SF-E811--828 concern','SF-E811--830 concern'))
out={'date_utc':now,'integrated':['SF-E829','SF-E830'],'canonical_sha256':hs,'new_rows':{'Q5ac':'refuted','Q5ad':'refuted'},'strictly_reduced_main_gates':['Q5i'],'new_balanced_seed':False}
(R/'research/support_actual_entries_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
