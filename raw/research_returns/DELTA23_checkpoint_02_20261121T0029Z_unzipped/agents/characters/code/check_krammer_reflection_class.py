#!/usr/bin/env python3
import pathlib,json,sys,numpy as np
import krammer_mixed_structure as k
HERE=pathlib.Path(__file__).resolve().parents[1]
d=json.loads((HERE/'records/krammer_mixed_correlation.json').read_text());a,b=[np.array(g) for g in d['pairs'][1]['unitary_generators']];Q=np.array(d['Q_unitary']);J=k.mm(Q,k.inverse(b))
# Conjugation by the two U generators equals conjugation by SU generators,
# since U=C4 (scalars) times SU and the determinant-one scalar correction exists.
key=lambda g:g.astype(np.int8).tobytes()
cl={key(J)};todo=[J]
for v in todo:
 for g in [a,b]:
  w=k.mm(k.mm(g,v),k.inverse(g));kw=key(w)
  if kw not in cl:cl.add(kw);todo.append(w)
sys.path.insert(0,str(HERE.parent/'pentagon'))
from krammer_f9_probe import to3
from krammer_first_pair import mul,inv
raw=lambda x:to3(np.array(x)).astype(np.int16)
C=raw(d['C_full']);Ci=inv(C);Q6=raw(d['Q_full']);Qi=inv(Q6);B=raw(d['pairs'][1]['splitting_basis']);Bi=inv(B)
def from3(g):
 return np.array([[int(g[2*i,2*j])+3*int(g[2*i+1,2*j]) for j in range(3)] for i in range(3)])
sol=np.load(HERE.parent/'pentagon/krammer_pentagon_solutions.npz');rows=[];counts={}
for ind,(R,lab) in enumerate(zip(sol['R'],sol['labels'])):
 r=mul(mul(Ci,R.astype(np.int16)),C);A=mul(mul(mul(Qi,r),Q6),inv(r));Au=from3(mul(mul(Bi,A),B)[6:,6:]);value=k.mm(J,Au);ok=key(value) in cl
 label=str(tuple(map(int,lab)));counts.setdefault(label,[0,0]);counts[label][int(ok)]+=1;rows.append({'index':ind,'pass':ok})
out={'scope':'Exact SU conjugacy check conditional on source reflection-frame comparison','J':J.tolist(),'SU_conjugacy_class_size':len(cl),'P7_counts_fail_pass':counts,'rows':rows}
(HERE/'records/krammer_reflection_class.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({x:out[x] for x in ['SU_conjugacy_class_size','P7_counts_fail_pass']},indent=2))
