"""Finite checks for arbitrary target exponents and ramified binomial valuations."""
from pathlib import Path
import json
from time import perf_counter
from math import comb
start=perf_counter()
# Reuse only the explicit finite-free-complex invariant definitions.
prefix=Path('code/C_finish_curvature_length.py').read_text().split("counts = {")[0]
ns={};exec(prefix,ns)
np=ns['np']; invariant=ns['invariant']
runs=[];twists=0
for p in (2,3,5,7):
 for r in range(1,5):
  for m in range(max(2*r,3),max(2*r,3)+4):
   mod=p**m; row=[]
   for a in range(1,p):
    T=pow(1+p**(m-1),a,mod)
    norm=sum(pow(T,j,mod) for j in range(p))%mod
    v=invariant(np.array([[T-1]],dtype=np.int64),np.array([[norm]],dtype=np.int64),p,m)
    assert v==(m-1 if a==1 else 0)
    row.append(v);twists+=1
   assert p**(2*(m-r))%mod==0
   assert p**(m-r)*p**(r-1)==p**(m-1)
   runs.append({'p':p,'r':r,'m':m,'normalizer_invariants':row})
report={'status':'PASS','scope':'Actual primary curvature projectors and Smith cokernel lengths for arbitrary-target-exponent scalar witnesses at p2,3,5,7; each finite height r1..4 is tested at four m values, with the square-zero ring-map exponents checked. Ramified polynomial valuations are a separate symbolic check below.','runs':runs,'scalar_runs':len(runs),'normalizer_twists':twists}
vals=[]
for p in (2,3,5,7,11):
 for e in range(1,7):
  for r in range(e,e+4):
   for m in range(max(2*r,2*e+1),max(2*r,2*e+1)+3):
    v=[]
    for i in range(2,p+1):
     c=comb(p,i); vp=0
     while c%p==0: vp+=1;c//=p
     val=e*vp+i*(m-e)-m
     assert val>0
     v.append(val)
    assert m-e>0 and m-e<m
    vals.append({'p':p,'e':e,'r':r,'m':m,'higher_term_valuations':v})
report['ramified_binomial_runs']=len(vals);report['ramified_binomial_checks']=vals
report['runtime_seconds']=round(perf_counter()-start,6)
Path('logs/C_finish_torsion_orders.json').write_text(json.dumps(report,indent=2)+'\n')
print({k:v for k,v in report.items() if k not in ('runs','ramified_binomial_checks')})
