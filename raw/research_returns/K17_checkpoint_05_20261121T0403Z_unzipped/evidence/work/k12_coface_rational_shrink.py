from pathlib import Path
from fractions import Fraction as F
import json
import sympy as sp
base=Path(__file__).parent
r=json.loads((base/'k12_coface_tripod_candidate.json').read_text())
target=r['target'];tri=[(i,j)for i in range(9)for j in range(i,9)]
E=sp.Matrix([[v[i]*v[j]*(1 if i==j else 2)for i,j in tri]for v in target]);piv=E.rref()[1];free=[j for j in range(45)if j not in piv];Einv=E[:,piv].inv()
old=[F(r['gram_rational'][i][j])for i,j in tri]
ns={};exec((base/'k12_survivor_certificate.py').read_text().split('INTEGER_GRAM =')[0],ns)
T={tuple(v)for v in target}|{tuple(-x for x in v)for v in target}
for den in [36,72,108,144,180,216,288,360,720]:
 x=[None]*45
 for j in free:x[j]=sp.Rational(round(old[j]*den),den)
 y=Einv*(sp.ones(13,1)-E[:,free]*sp.Matrix([x[j]for j in free]))
 for j,z in zip(piv,y):x[j]=z
 q=[[F(0)for j in range(9)]for i in range(9)]
 for (i,j),z in zip(tri,x):q[i][j]=q[j][i]=F(int(z.p),int(z.q))
 try:sv,nodes,diag=ns['exact_short_vectors'](q,F(1))
 except AssertionError: print(den,'not PD',flush=True);continue
 print(den,len(sv),nodes,flush=True)
 if set(sv)==T and all(ns['gram_value'](q,v)==1 for v in target):
  r.update(gram_rational=[[str(z)for z in row]for row in q],short_vectors=[list(v)for v in sv],nodes=nodes,diagonal=[str(z)for z in diag])
  (base/'k12_coface_tripod_candidate.json').write_text(json.dumps(r,indent=2)+'\n')
  print('SHRUNK',den,flush=True);break
