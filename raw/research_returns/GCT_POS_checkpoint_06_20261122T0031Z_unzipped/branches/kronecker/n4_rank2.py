import sympy as s,json,itertools,time
from pathlib import Path
p=Path(__file__).resolve().parent
obj=json.loads((p/'dyadic_n4_stabilizers.json').read_text())
x=s.symbols('x0:4'); inds=list(itertools.combinations(range(4),3))
for idx,rec in enumerate(obj['records']):
 sets=rec['spectra']; S=[tuple(sets[j].index(e[j]) for j in range(3)) for e in rec['aggregate_support']]
 rec['rank2_chart_groebner']=[]
 for a in range(3):
  b,c=[j for j in range(3) if j!=a];Q=s.zeros(4)
  for e in S:Q[e[b],e[c]]+=x[e[a]]
  eq=list({s.expand(Q.extract(I,J).det()) for I in inds for J in inds}-{s.Integer(0)})
  charts=[]
  for k in range(4):
   # last nonzero coordinate xk=1
   sub={x[k]:1,**{x[j]:0 for j in range(k+1,4)}}
   ee=[e.subs(sub) for e in eq]
   if k==0:gg=ee
   else:gg=list(s.groebner(ee,*x[:k],order='lex'))
   charts.append([str(v) for v in gg])
  rec['rank2_chart_groebner'].append(charts)
  print(idx+1,a,charts,flush=True)
(p/'dyadic_n4_rank2.json').write_text(json.dumps(obj,indent=2))
