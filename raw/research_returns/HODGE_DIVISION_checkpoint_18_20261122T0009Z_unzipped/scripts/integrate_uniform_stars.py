"""Integrate the independently whole-reviewed E832 and E832R star obstructions."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json
R=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
paths={'E832':'agents/sixfolds/rm_elliptic_star_character_obstruction_section.tex','E832R':'agents/sixfolds/rm_reversed_elliptic_star_addendum_section.tex'}
hs={'E832':'98f520c95196842a207490db13ae83d9b725ab91dd91aaa73d0eb83a50191893','E832R':'cd2a3c9cef1ab2406dadf9f7913d49195606884607643789a0d631adcd49ec57'}
for k,p in paths.items(): assert hashlib.sha256((R/p).read_bytes()).hexdigest()==hs[k]
def ch(s,a,b):
    assert s.count(a)==1,(a,s.count(a))
    return s.replace(a,b)
q=R/'QUESTIONS.tsv'
rs=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rs[0])
assert all(r['id']!='Q5af' for r in rs)
(R/'research/gate_before_uniform_stars.json').write_text(json.dumps({r['id']:r for r in rs if r['id']=='Q5i'},indent=2)+'\n')
p=R/'HODGE_DIVISION.tex';s=p.read_text()
anchor=r'\input{agents/sixfolds/rm_vertexwise_coupling_gate_section.tex}'
s=ch(s,anchor,anchor+'\n'+'\n'.join(r'\input{'+p+'}' for p in paths.values()))
s=ch(s,'These incidence conditions do not assert geometric realizability.\nRank-deficient unit matrices,',r'''These incidence conditions do not assert geometric realizability.
SF-E832 and E832R exclude actual elliptic stars with either uniform
semipositive sign, for arbitrary rational algebraic $B$ and every
specified coherent effective finite action in E825's scope.
The actual locally split extension identifies the defect bundle as
$(L|_{S_2})^r$; its necessary determinant condition gives two positive
RM block traces. The completed-square second-character equation then
contradicts a universal compound-matrix lemma. For scalar adjusted
unit direction, the character obstruction already permits mixed signs.
General mixed-sign and multicenter configurations remain outside
these two statements.
Rank-deficient unit matrices,''')
p.write_text(s)
gate=('SF-E832/E832R exclude every actual single-center elliptic star of either uniform semipositive sign in the specified unit/free extension architectures, for arbitrary rational algebraic B and every coherent effective finite action in E825 scope. Local splitting and the actual ring map identify the defect bundle as (L|S2)^r; E825 forces the adjusted unit to preserve both RM planes with traces7k. The first two character equations give b^2-kappa*u^2=d*(theta+^2+theta-^2), kappa>0,d!=0, with b or -b semipositive, contradicting the universal compound lemma. Scalar adjusted unit directions are excluded for either or mixed signs without that positivity hypothesis. General mixed-sign stars and multiple centers remain outside these statements. ')
for r in rs:
    if r['id']=='Q5i':
        r['finding_ids_or_current_gate']=ch(r['finding_ids_or_current_gate'],'Remaining: unstable bundles',gate+'Remaining: unstable bundles').replace('outsideE818/E821/E822/E823/E824/E825/E826/E827/E828/E829/E830/E831','outsideE818/E821/E822/E823/E824/E825/E826/E827/E828/E829/E830/E831/E832/E832R')
rs.append(dict(zip(fields,['Q5af','Prompt target5; actual elliptic stars and the E825 defect determinant','Can a uniformly signed actual elliptic star compensate the unit character to produce a balanced weakly semiregular RM seed?','refuted',gate+'Root and G34 complete proof reviews PASS; no new seed or multicenter exclusion is claimed.'])))
with q.open('w',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rs)
events=[
('SF-E832','targeted proof check','Root read the entire294-line frozen draft0542dce98bcf06689930578a262dd242b43cfbc0a3f2aebaec263222b38d01ad, whole author checker, complete conversion record, and all316 canonical TeX lines at98f520c9. Full PASS: compound interpretation, scalar graph proof, deficient-rank support-plane argument, tensor factorization, opposite determinant signs, completed square and exact E825 extension interface. E825 full sections1-2 and6-7 and determinant trace interface reread. The real indefinite boundary matrices are not asserted to be rational classes or objects.',paths['E832']),
('SF-E832R','targeted proof check','Root read all94 frozen draft lines atdc18d6bf237e6133a4f86a74c466d3962380a2b8cbb48f440931012bc8877446, all100 canonical lines atcd2a3c9c and complete conversion record. PASS reversed actual A/B architecture, local FF transition and intrinsic determinant, b to minus b reduction and empty-leaf case. No new computation claimed.',paths['E832R']),
('SF-E832/E832R independent audit','targeted proof check','G34 whole proof/source-interface/author-code review PASS for E83220:55:32UTC and separate full E832R reading20:58:56UTC. Root read entire combined report SHAe6885a6c8d57d0c0cb08293ba9a0f59bf4d59fd51ecd2238064676c8b021fe2f. Peer separately authored exact supplement took0.038822864s for rational expansion, completed square,15graphs, generic block compound, determinant product, rank cases and boundary matrices. Initial SymPy structural comparison failure retained and repaired by exact zero-difference predicate. Root does not claim whole peer-code reading.','agents/g34_eightfolds/bireflection/ELLIPTIC_STAR_PEER_AUDIT.md'),
('SF-E832 author exact supplement','computation or formal certificate','Author actual0.053802978s PASS unit coefficients1,0,0,-2,4; completed square;15four-edge graphs (12withtriangle,3cycles); determinant-product and printed boundary compound identities. Root read entire checker and output. No computational certification of universal positivity or categorical gluing claimed.','agents/sixfolds/rm_elliptic_star_character_certificate.py; agents/sixfolds/rm_elliptic_star_character_certificate_output.json'),
('SF-E825 used by E832/R','used and rechecked in this run','Root and peer reopened the actual unital defect ring map, products through free modules, fixed normal-frame removal, rational-B transport and simultaneous-kernel condition. Published BF and supplied S21 status remain exactly as in E825; no new external source premise or preservation of a filtration by the action is assumed.','agents/sixfolds/rm_free_summand_overlap_section.tex')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Uniform-sign elliptic-star gates integrated\n\n'+now+' — Q5af refuted and Q5i strictly reduced. '+gate+'This is not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Character obstruction for actual elliptic stars\n\n'+gate+'In the condition-A supplier problem (cote16 scan050), this removes two concrete coherent K-theory architectures. The obstruction uses the lambda-ring/exterior-square character and the actual defect determinant; positivity is a constraint on the proposed object, not a cycle supplier. The common EGA/SGA/realization locators, condition-I division and Cayley-Hamilton projector framework remain as recorded. No implication for all unstable sheaves or perfect complexes is claimed.\n')
p=R/'research/frameworks.tex';p.write_text(ch(p.read_text(),'SF-E811--831 concern','SF-E811--832R concern'))
out={'date_utc':now,'integrated':['SF-E832','SF-E832R'],'reviewed_canonical_sha256':hs,'new_rows':{'Q5af':'refuted'},'strictly_reduced_main_gates':['Q5i']}
(R/'research/uniform_stars_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
