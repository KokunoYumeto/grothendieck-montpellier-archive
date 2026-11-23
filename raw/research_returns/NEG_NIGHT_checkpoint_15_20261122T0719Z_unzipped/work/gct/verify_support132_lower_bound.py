"""Independent exact integer certificate: original132-support lifts cost>=344.
No floating arithmetic, optimizer, assumed equal actions, or grading cutoff.
The verifier enumerates self-square c,b directly rather than using the
closed-form minimizer in the exploratory finder.
"""
from pathlib import Path
from math import isqrt,lcm
from functools import lru_cache
import json
import sympy as sp

BASE=Path('work/gct');q,v=sp.symbols('q v');D=q+2+q**-1;C=D-1
raw=json.loads(Path('sources/OURS_E4_scripts/e3_constants.json').read_text())
trace={};mass={}
for r in raw:
 key=tuple(r[k] for k in ('b','bp','bpp'))
 poly=sp.Poly(sp.expand(sp.sympify(r['c'],locals={'v':v})*v**64),v)
 a={}
 for (j,),co in poly.terms():
  assert co.is_Integer and (j-64)%2==0
  a[(j-64)//2]=int(co)
 trace[key]=a;mass[key]=sum(abs(c) for c in a.values())
assert len(trace)==132 and sum(mass.values())==4443
nonunit={k:m for k,m in mass.items() if 'mu' not in k[:2]}
assert len(nonunit)==113 and sum(nonunit.values())==4424
names=[f'g{i}_{w}' for i in (1,2) for w in ('1','12','2','21')]
assert mass['Sigma','Sigma','Sigma']==576
for b in names:
 assert mass['Sigma',b,'Sigma']==(48 if b.endswith(('_1','_2')) else 192)
 assert trace['Sigma',b,'Sigma']==trace[b,'Sigma','Sigma']
 assert sum(trace['Sigma',b,'Sigma'].values())%2==0
assert all(sum(a.values())%2==0 for k,a in trace.items() if 'mu' not in k[:2])
for b in names:
 c0=16 if b.startswith('g2_') and b.endswith(('12','21')) else 8
 b0=4 if b.endswith(('_1','_2')) else 64
 assert mass[b,b,b]==c0 and mass[b,b,'Sigma']==b0
within_other=0;cross=0
for (a,b,z),m in nonunit.items():
 if a=='Sigma' or b=='Sigma':continue
 if a[1]!=b[1]:cross+=m
 elif a!=b:within_other+=m
assert cross==800 and within_other==776
# Check the four exact source parities used to force S(1) divisible by4.
def parity_equal(key,p):
 shifted=sp.Poly(sp.expand(p*q**64),q)
 expected={j[0]-64:int(c)%2 for j,c in shifted.terms() if int(c)%2}
 actual={j:c%2 for j,c in trace[key].items() if c%2}
 return expected==actual
assert parity_equal(('Sigma','Sigma','Sigma'),0)
assert parity_equal(('Sigma','g1_1','Sigma'),0)
assert parity_equal(('Sigma','g2_1','Sigma'),D**2*C)
assert parity_equal(('g1_1','g2_1','Sigma'),D)

PAIR_CAP=343;ADDED=2*PAIR_CAP;TARGET=4424+ADDED
@lru_cache(None)
def exact_self_cost(s,x,c0,b0):
 # Direct finite enumeration; c<x because bottom coefficient is positive.
 values=[]
 for c in range(c0,x,2):
  numerator=x*x-c*x
  if numerator%s:continue
  b=numerator//s
  if b>=b0 and b%2==0:values.append(c+b)
 return min(values) if values else None

def divisors(n):
 ans=[]
 for d in range(1,isqrt(n)+1):
  if n%d==0:
   ans.append(d)
   if d*d!=n:ans.append(n//d)
 return sorted(ans)

def cell_dp(s,div,cword):
 step=lcm(div,2);remainder=ADDED-(s-576)
 cap=480+remainder//2;dp={0:0}
 for lower,c0,b0 in [(48,8,4),(48,8,4),(192,cword,64),(192,cword,64)]:
  options=[]
  for x in range((lower+step-1)//step*step,lower+remainder//2+1,step):
   cost=exact_self_cost(s,x,c0,b0)
   if cost is not None:options.append((x,cost))
  if not options:return {}
  nxt={}
  for total,cost in dp.items():
   for x,y in options:
    if total+x>cap:continue
    if cost+y<nxt.get(total+x,10**20):nxt[total+x]=cost+y
  dp=nxt
  if not dp:return {}
 return dp

minimum=None;best=[];rows=0;nonempty=0;comparisons=0
for s in range(576,576+ADDED+1,4):
 cache={}
 for a in divisors(2*s):
  b=2*s//a;rows+=1
  if (a,8) not in cache:cache[a,8]=cell_dp(s,a,8)
  if (b,16) not in cache:cache[b,16]=cell_dp(s,b,16)
  left,right=cache[a,8],cache[b,16]
  if not left or not right:continue
  nonempty+=1
  for A,costA in left.items():
   for B,costB in right.items():
    comparisons+=1
    assert (2*A*B)%s==0
    lower=s+2*(A+B)+2*A*B//s+776+costA+costB
    if minimum is None or lower<minimum:minimum=lower;best=[]
    if lower==minimum:best.append([s,a,b,A,B,costA,costB,lower])
    assert lower>TARGET
assert minimum==5112 and (minimum-4424)//2==344
out={'original_positions':132,'specified_nonunit_positions':113,'original_nonunit_mass':4424,'pair_budget_excluded':343,'total_mass_budget_excluded':5110,'S_range':[576,1260,4],'divisor_rows_checked':rows,'nonempty_rows':nonempty,'cell_sum_comparisons':comparisons,'minimum_relaxation_mass':minimum,'minimum_rows':best,'proved_pair_lower_bound':344,'scope':'Every exact132-support normalized-unit effective lift,with arbitrary finite Laurent grading and no symmetry assumption. Necessary relaxation only;no realization or all810-position claim.'}
(BASE/'support132_lower_bound_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
