import sympy as s,json,itertools
from pathlib import Path
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
obj=json.loads((p/'dyadic_n4_stabilizers.json').read_text())
perms=list(itertools.permutations(range(4)))
for idx,rec in enumerate(obj['records']):
 sets=rec['spectra'];S={tuple(sets[j].index(e[j]) for j in range(3)) for e in rec['aggregate_support']}
 I=s.Matrix([[int(e[j]==v) for e in sorted(S)] for j in range(3) for v in range(4)])
 snf=smith_normal_form(I,domain=ZZ);diag=[abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]
 auto=[]
 for a,b,c in itertools.product(perms,repeat=3):
  if {(a[i],b[j],c[k]) for i,j,k in S}==S:auto.append([a,b,c])
 rec['incidence_smith_diagonal']=diag;rec['support_perm_autos']=auto
 print(idx+1,diag,'autos',len(auto),auto,flush=True)
(p/'dyadic_n4_monomial.json').write_text(json.dumps(obj,indent=2))
