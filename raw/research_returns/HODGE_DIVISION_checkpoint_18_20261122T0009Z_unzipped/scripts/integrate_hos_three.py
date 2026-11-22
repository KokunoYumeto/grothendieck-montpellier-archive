"""Integrate the selfdual-only higher F3 source obstruction after whole reviews."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
proof='agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_section.tex'
frozen='43d9154af45a2042e1cbbd5a0f536a7f932e0cad351e29e980a1ca5b3d65dae9'
assert hashlib.sha256((R/proof).read_bytes()).hexdigest()==frozen
def ch(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
q=R/'QUESTIONS.tsv';rs=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rs[0]);assert all(r['id']!='Q2br' for r in rs)
(R/'research/gate_before_hos3.json').write_text(json.dumps({r['id']:r for r in rs if r['id']=='Q2i'},indent=2)+'\n')
p=R/proof;p.write_text(ch(p.read_text(),'This new proof is awaiting independent review. It uses the complete','This new proof has passed complete mathematical reviews by /root and\n/root/imprimitive. Both read the entire author checker and its output;\nthe peer also supplied a separately authored exact arithmetic certificate.\nIt uses the complete'))
p=R/'HODGE_DIVISION.tex';s=p.read_text();a=r'\input{agents/g34_eightfolds/bireflection/higher_odd_symplectic_five_section.tex}';s=ch(s,a,a+'\n'+r'\input{'+proof+'}')
s=ch(s,'Thus only $q=3$ remains among the single-field higher odd-symplectic\ncases.',r'''D-HOS-11 supplies full-normalizer support $13e/108$ for every
ordinary higher $q=3$ factor. D-HOS-12 excludes all self-dual such
factors, also allowing arbitrary mixtures with the $q=5$ factors:
the nontrivial multiplier gives $e\le324/11<30$, and exact integer
costs exclude all three remaining degrees $27,28,29$. Nonselfdual
higher $q=3$ factors remain open among these single-field cases.''');p.write_text(s)
gate=('D-HOS-11 proves full-normalizer support13/108 for every ordinary higherSp(q3) factor. D-HOS-12 excludes every selfdual such factor, allowing arbitrary mixtures withq5 and all compatible tensor permutations/scalars: nontrivial multiplier gives e<=324/11<30 and exactceilings exclude27,28,29 against floor27. Nonselfdual higherq3 factors remain open. ')
for r in rs:
 if r['id']=='Q2i':r['finding_ids_or_current_gate']=ch(r['finding_ids_or_current_gate'],'Onlyq3 remains among single-field higher odd-symplectic cases; ',gate)
rs.append(dict(zip(fields,['Q2br','Prompt target2; selfdual higher symplectic q3 factors','Can selfdual higherSp(q3) cores, possibly mixed withq5 factors, survive the actual rank-nine source budget?','refuted',gate+'Whole root/peer mathematical/source/code reviews PASS. No nonselfdual exclusion or character-table premise.'])))
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rs)
events=[
 ('D-HOS-11--12','targeted proof check','Root read all185lines at43d9154a, entire author exact program and entire JSON. Whole mathematical PASS: both similitude multipliers, anisotropic equal-coefficient shear, exact1/4/4phase counts, universal carrier and linear-weight bounds, full tensor normalizers, selfdual-only source multiplier, exact endpoint ceilings. Canonical status paragraph alone changed.',proof),
 ('D-HOS-11--12 independent audit','independent re-proof','Imprimitive full proof/source/author-code review PASS20:49:41UTC. Root read complete report SHA8718af16d4607dbe19a33b12b0098f086ae3d7c9651fb66386cad3fbfcab7912. Independent exact run0.449292201s:48GSp2/576commutators,729selfadjoint matrices72solutions11520cases,81648Weyl-entry identities and exactceilings. No authorcode imported; root does not claim whole peer-code reading.','agents/imprimitive/audit_symplectic_three/PEER_AUDIT.md'),
 ('D-HOS-11--12 sources and computed scope','carried as background without fault found','Root reuses prior complete HOS02/07-10 proofs and exact HHM35/4 plus LiXia14 cover/automorphism scope. Peer freshly reread those full source passages. No new Weil-character classification, reality of allq3 characters, or finite table is assumed. Author actual finite supplement0.050566796s retained; no fresh root rerun claimed.','agents/g34_eightfolds/bireflection/check_higher_symplectic_three.py; agents/g34_eightfolds/bireflection/check_higher_symplectic_three.json')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Selfdual higher symplectic q3 gate closed\n\n'+now+' — Q2br refuted; Q2i strictly reduced. '+gate+'Both complete proofs have root and independent peer checks; the normalizer theorem has broader character scope than the geometric exclusion and these are kept distinct. This is not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## The remaining higher symplectic source must use nonselfdual q3 factors\n\n'+gate+'This is a necessary restriction on the actual weight-one finite-monodromy condition-A supplier gate, cote16 scan050. It supplies no new cycle and gives no existence inference for the surviving factors. EGA/SGA and realizations retain the common-framework placement; condition-I positivity, Cayley-Hamilton division, motivic/L-function scope and conditional inputs are unchanged.\n')
out={'date_utc':now,'integrated':['D-HOS-11','D-HOS-12'],'reviewed_sha256':frozen,'canonical_sha256':hashlib.sha256((R/proof).read_bytes()).hexdigest(),'new_rows':{'Q2br':'refuted'},'strictly_reduced_main_gates':['Q2i']}
(R/'research/hos3_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
