"""Integrate OL04--05 and E831 with their exact reviewed scopes."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
paths={'OL4':'agents/imprimitive/orthogonal_lowlevels/orthogonal_lowlevel_section.tex','E831':'agents/sixfolds/rm_vertexwise_coupling_gate_section.tex'}
hs={'OL4':'2f40c6daf6ead0f9cad0aa0ac77f1fb9699b55396c215cc3c24c3f34cd9894e7','E831':'9bfbaf787267c0a6e862117b18208176d197cf139bd2a3ba2f3c9a684a497760'}
for k,p in paths.items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==hs[k]
def ch(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
q=R/'QUESTIONS.tsv';rs=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rs[0]);assert all(r['id'] not in ('Q2bq','Q5ae') for r in rs)
(R/'research/gates_before_lowlevel_vertexwise.json').write_text(json.dumps({r['id']:r for r in rs if r['id'] in ('Q2i','Q5i')},indent=2)+'\n')
p=R/paths['OL4'];p.write_text(ch(p.read_text(),'statements and exact author certificate have passed an author check;\nindependent reviews are pending.','statements and exact author certificate have passed the author check\nand complete independent mathematical reviews by /root and\n/root/g34\\_eightfolds. The peer also supplied a separately authored\nexact supplement; all actual scopes and timings are recorded.'))
p=R/'HODGE_DIVISION.tex';s=p.read_text()
for a,b in [('agents/imprimitive/orthogonal_levels/orthogonal_level_section.tex',paths['OL4']),('agents/imprimitive/orthogonal_levels/orthogonal_level_bibitems.tex','agents/imprimitive/orthogonal_lowlevels/orthogonal_lowlevel_bibitems.tex'),('agents/sixfolds/rm_actual_elliptic_coupling_gate_section.tex',paths['E831'])]:
 anchor=r'\input{'+a+'}';s=ch(s,anchor,anchor+'\n'+r'\input{'+b+'}')
s=ch(s,'The remaining ordinary low-level natural dimension is unbounded;\nno theta irreducibility or full orthogonal extension is asserted.',r'''The remaining ordinary low-level natural dimension is unbounded;
no theta irreducibility is used. D-OL-04--05 then proves that a level
$\ell$ ordinary character extends irreducibly to the full orthogonal
group, and is self-dual, whenever $d\ge4\ell+2$. The proof compares
actual ordered-tuple orbits and their commutant algebras.
Thus a nonselfdual ordinary factor has $d\le4\cdot10^{30}-3$.
For $d\ge4\cdot10^{30}-2$ every factor is ordinary and self-dual;
the actual inducing image has a nontrivial bilinear-form multiplier.
The published ratio estimate at $q\ge16$ then forces $e\le64$,
contradicting the factor-degree bound. The unbounded natural-dimension
case is therefore confined to $q\in\{2,3,4,5,7,8,9,11,13\}$ and
ordinary self-dual characters of level below $10^{30}$.''')
s=ch(s,'selected unit-block vanishings retained.\nRank-deficient unit matrices,',r'''selected unit-block vanishings retained.
SF-E831 strengthens this to a separate support space $Z_v$ at each
actual selected block: invariant middle Ext is at least
$\sum_v(6-\dim Z_v-\dim\operatorname{rad}(q_\wedge|_{Z_v}))$.
At most three selected blocks can be untouched by actual exceptional
components. For $N>3$ selected blocks, at least
$\lceil(N-3)/2\rceil$ active exceptional pairs are required, or
$\lceil3(N-3)/2\rceil$ if every pair support has dimension at most one.
Its weighted inequality retains the distinction between one and two
selected endpoints. The zero-survivor three-spaces are classified
explicitly as $a\wedge V$ or $\Lambda^2H$, $\dim H=3$.
These incidence conditions do not assert geometric realizability.
Rank-deficient unit matrices,''');p.write_text(s)
ol=('D-OL-04--05 proves actual fullO extension and selfduality for ordinary level-ell characters when d>=4ell+2 by equality of tuple orbits and commutants. Thus every nonselfdual ordinary factor has d<=4*10^30-3. At d>=4*10^30-2 all factors are ordinary/selfdual and the inducing image has a nontrivial multiplier; q>=16 then gives e<=64 contradicting the k1degreefloor. The unbounded naturald gate is now ordinary selfdual level<10^30 over exactlyq∈{2,3,4,5,7,8,9,11,13}. ')
ve=('SF-E831 uses separate actual support spacesZv at each selected block, giving ext2Gamma>=sum_v(6-dimZv-dimrad). At most3selectedblocks may have no actual exceptional component; the weighted necessary budget is sum_ab(1+1_b∈J)dimZab>=3N-9. ForN>3, at leastceil((N-3)/2)activepairs, orceil(3(N-3)/2)ifallsupportdims<=1, are needed. Zero-survivor3spaces are exactlya∧V orLambda2H. Actualfiltration/action/unitExt3 hypotheses remain; hypotheticalincidence data are not objects. ')
for r in rs:
 if r['id']=='Q2i':r['finding_ids_or_current_gate']=ch(r['finding_ids_or_current_gate'],'Other small-field higher-rank Lie cores remain.',ol+'Other small-field higher-rank Lie cores remain.')
 if r['id']=='Q5i':r['finding_ids_or_current_gate']=ch(r['finding_ids_or_current_gate'],'Remaining: unstable bundles',ve+'Remaining: unstable bundles').replace('outsideE818/E821/E822/E823/E824/E825/E826/E827/E828/E829/E830','outsideE818/E821/E822/E823/E824/E825/E826/E827/E828/E829/E830/E831')
rs.extend(dict(zip(fields,x)) for x in [
 ['Q2bq','Prompt target2; ordinary orthogonal low levels and reality','Can an unbounded-natural-dimension transitive orthogonal source retain nonselfdual ordinary factors or field size at least16?','refuted',ol+'Whole root/G34 mathematical/source/code reviews PASS; finite orbit calculations are supplemental.'],
 ['Q5ae','Prompt target5; blockwise actual exceptional support','Can one actual exceptional coupling erase diagonal classes at unrelated blocks or can an insufficiently covered support graph give a balanced seed?','refuted',ve+'Whole root/G34 proof reviews and separately authored exterior/incidence checks PASS.']])
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rs)
events=[
 ('D-OL-04--05','targeted proof check','Root read entire231-line proof, bibliography, source log, all114lines authorchecker and completeJSON. Whole mathematical PASS: complement in polar radical quotient, both-characteristic stabilizer quotient surjection, equality of actual commutant algebras, irreducible extension/reality, imaginary-field multiplier and full-normalizer/source bound. Duplicate local tags corrected consistently toOL4.1-12; externalOL.1 retained. Finalfrozen2f40c6da checked; status-only canonical change.',paths['OL4']),
 ('D-OL-04--05 primary inputs','used and rechecked in this run','Root freshly opened published KTV2023 journalPDF and read allprintedpp39-44, including odd/even fullO strong reality, both quotient descriptions, orthogonal-sum compatibility and Th1. Published restatements used; no fresh original Wonenburger/Ellers-Nolte/Gow proofs claimed. Earlier full GLT160/165 and DHP4.1(2)p141 checks retained, exact new application rechecked.','agents/imprimitive/orthogonal_lowlevels/SOURCES.md'),
 ('D-OL-04--05 independent audit','independent re-proof','G34 full proof/source/author-code review PASS20:52:53UTC on2f40c6da; root read entire report SHA2b875a19cc465c56b45036eb5ec8679be90e99b21f26f06ff3b6f63a59ceb1a0. Own exact0.221892491s:4096pair states15orbits,715stabilizer spans,1364binaryforms and constants. No independent group-order rerun claimed; root does not claim whole peer-code reading.','agents/g34_eightfolds/bireflection/ORTHOGONAL_LOWLEVEL_PEER_AUDIT.md'),
 ('D-OL-04--05 author computation','computation or formal certificate','Author final actual0.736255367s certificate binds tag-repaired hash:40320generated orthogonal matrices,20160derived subgroup,4096pairs15equalorbits,715spans,3048binaryforms and exactconstants. Full root code/output reading; no root rerun claimed. The finite d6witness supplements the universal d>=10 theorem.','agents/imprimitive/orthogonal_lowlevels/check_lowlevel.py; agents/imprimitive/orthogonal_lowlevels/lowlevel_checked.json'),
 ('SF-E831','targeted proof check','Root read all249draft lines at870daf and all256canonical lines at9bfbaf78, plus entire authorchecker. PASS separate vertex annihilators, both actual LES boundaries, separate quotient traces, invariant averaging, exact weighted budgets and full maximal-isotropic3space classification. The32vertex capacities are necessary only; no new realization claimed.',paths['E831']),
 ('SF-E831 independent audit','independent re-proof','G34 full proof/dependency/author-code review PASS20:47:16UTC; root read complete report SHAd9e7a6df1588fb284669754d85ddaa00c49e5f9fb5cfe0a2805fd4680904b7e2. Own exact0.033433267s reconstructs annihilator ranks, both isotropic families under3basis changes, hypothetical6vertex example and97budgets. Root does not claim whole peer-code reading. No new external premise.','agents/g34_eightfolds/bireflection/VERTEXWISE_COUPLING_PEER_AUDIT.md')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Orthogonal reality and vertexwise coupling gates integrated\n\n'+now+' — Q2bq and Q5ae refuted; both Q2i and Q5i strictly reduced. '+ol+ve+'All complete proofs have independent whole readings. These strengthen previous gates and are not counts of new successful suppliers. This is not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Reality of low levels and local support coverage\n\n'+ol+ve+'These restrict the actual condition-A supplier alternatives, cote16 scan050, in finite-monodromy weight-one variations and in coherent balanced-RM objects respectively. No surviving profile is promoted to a source. Common EGA/SGA/realization placement, condition-I division, Cayley-Hamilton inversion, motivic/L-function scope and conditional Markman/Severn/032 status remain unchanged.\n')
p=R/'research/frameworks.tex';p.write_text(ch(p.read_text(),'SF-E811--830 concern','SF-E811--831 concern'))
out={'date_utc':now,'integrated':['D-OL-04--05','SF-E831'],'reviewed_sha256':hs,'canonical_sha256':{k:hashlib.sha256((R/v).read_bytes()).hexdigest() for k,v in paths.items()},'new_rows':{'Q2bq':'refuted','Q5ae':'refuted'},'strictly_reduced_main_gates':['Q2i','Q5i']}
(R/'research/lowlevel_vertexwise_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
