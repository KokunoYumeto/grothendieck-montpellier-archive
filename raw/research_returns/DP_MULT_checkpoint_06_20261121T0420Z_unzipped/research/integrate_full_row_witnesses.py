#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
root=Path(__file__).resolve().parents[1];r=root/'research';now=datetime.now(timezone.utc).isoformat()
main=root/'DP_MULT.tex';s=main.read_text()
scopes={
 63:'Read COMPLETE corrected saved memo sections1-7 and COMPLETE intended proposition/proof. Checked all HC fields including m=2 and every epsilon index, fixed residual partitions, word equations, unique diagonal monomial and exact lowest-degree factorial extraction, actual product copy assignment, its explicitly abstract row labels, integral product jet generation, finite multilinear tuple extraction and the upper valuation/asymptotic claim. Then read the only product-span clarification: finite integral generating family suffices, with no full H0 product-space identification asserted.',
 65:'Read COMPLETE saved memo sections1-8 and COMPLETE intended proposition/proof. Checked actual conjugated E action, Rosati and trace-one line isomorphisms, true characters3/2 and all multiplicity rows, explicit per-embedding HC formulas and residual partitions, every conjugate contraction and row-invariance case, exact fixed factorial extraction, first-column mixed coefficient and Legendre valuation, alpha/baralpha swap, product jet generation, finite integral tuple extraction and all generalized-type/SizeData/theta-image boundaries. Then read the only product-span clarification; no full H0 product-space identification is needed.'
}
for n,fn in [(63,'scalable_row_prefactor_DP63.md'),(65,'embedding_labelled_harmonic_witness_DP65.md')]:
 fragment=(r/f'DP{n}_integrated_fragment.tex').read_text()
 assert f'\\label{{DP{n}}}' not in s
 anchor='\\subsection{The bare prime budget for every fixed cyclotomic type}' if n==63 else '\\section{Cote 54, Cartier duality, and the crystalline setting}'
 assert s.count(anchor)==1;s=s.replace(anchor,fragment+'\n\n'+anchor)
 d={'statement':f'DP{n}','recorded_utc':now,'who':'/root','model':'GPT-6 Astra Pro','effort':'not exposed by runtime','type':'targeted proof check','scope':scopes[n],'outcome':'PASS complete saved memo and intended proof, with explicitly read targeted clarification; mathematical reading, not formal verification.','files':[{'path':f,'sha256':hashlib.sha256((r/f).read_bytes()).hexdigest()} for f in (fn,f'DP{n}_integrated_fragment.tex')]}
 (r/f'DP{n}_root_integrated_review_metadata.json').write_text(json.dumps(d,indent=2)+'\n')
main.write_text(s)
def read(p):
 with p.open(newline='') as f:
  x=csv.DictReader(f,delimiter='\t');return x.fieldnames,list(x)
def write(p,f,rows):
 with p.open('w',newline='') as o:
  w=csv.DictWriter(o,f,delimiter='\t');w.writeheader();w.writerows(rows)
ef,es=read(root/'CHECK_EVENTS.tsv')
for n in (63,65):
 d=json.loads((r/f'DP{n}_root_integrated_review_metadata.json').read_text());ev=f'research/DP{n}_root_integrated_review_metadata.json'
 if not any(x['evidence']==ev for x in es):
  serial=max(int(x['event_id'].split('-')[1]) for x in es)+1
  es.append(dict(zip(ef,[f'DPC-{serial:03d}',f'DP{n}','2026-11-21 UTC',now,'/root','GPT-6 Astra Pro','not exposed by runtime','DP_MULT_20261121','targeted proof check',d['scope'],d['outcome'],ev])))
write(root/'CHECK_EVENTS.tsv',ef,es)
qf,qs=read(root/'QUESTIONS.tsv');ids={x['id'] for x in qs}
newqs=[
 ('Q3ay','DP63;DP61;DP58;DP59','Can varying HC partitions admit a nonzero completed sharp jet with bounded filler cost?','proved with explicit chosen-direction scope','DP63','Explicit HC data have A=A*+ae0,B=B*+be0 with fixed residual partitions. The integral diagonal monomial gives exact factorial cost independent of a,b. On an actual fixed J product some generic allowed tuple has valuation at most (11^r-1)/10+fixed cost at M=O(total degree). Abstract rows are not identified with CM conjugate labels by this result.'),
 ('Q3az','DP65;DP49(JT7);DP58(ES11-12);DP61 source harmonic equations','Can every actual CM-labelled row be filled while retaining the sharp local rate in a genuine generalized harmonic module?','proved','DP65','On J^P times conjugate-action J^Q, the critical characters3 and2 are distinct positive embeddings. Their monomial is harmonic for every actual conjugate contraction. Fixed determinant fillers realize all positive/negative rows; a fixed integral prefactor gives exact constant factorial cost. Some permitted tuple has rate at most1/1220. The type is genuinely Phi123, not the old induced type; a full SizeData2 package and iterated theta image remain.')]
for q in newqs:
 if q[0] not in ids:qs.append(dict(zip(qf,q)))
for q in qs:
 if q['id']=='Q3e':
  q['finding_ids_or_counterexample']='U2;DP25-DP65'
  q['current_gate_or_scope']+=' DP63/65 now close the nonzero full-row local section interface in the explicit varying HC family: actual embedding-labelled generalized HaO witnesses and generic allowed translates retain rate at most1/1220 with fixed filler cost. Remaining compatibility concerns one common unramified host/moduli/CM type, its actual iterated theta image and full quantitative SizeData2/source-cost inputs, not the bare existence of such full-row local witnesses.'
write(root/'QUESTIONS.tsv',qf,qs)
print(json.dumps({'recorded_utc':now,'integrated':[63,65],'events':len(es),'questions':len(qs),'main_bytes':main.stat().st_size}))
