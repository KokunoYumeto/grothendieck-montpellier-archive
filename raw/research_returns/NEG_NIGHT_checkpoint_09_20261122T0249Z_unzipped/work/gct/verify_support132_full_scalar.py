"""Independent exact integer certificate: original132-support lifts cost>=560.
No floating arithmetic, optimizer, assumed equal actions, or grading cutoff.
The verifier regenerates all weak rows directly and enumerates the
remaining cell coefficients using a different divisor parameter.
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

from itertools import product
from collections import defaultdict

PAIR_CAP=559;BUDGET=2*PAIR_CAP;MASS_CAP=4424+BUDGET
@lru_cache(None)
def divisors(n):
 ans=[]
 for d in range(1,isqrt(n)+1):
  if n%d==0:
   ans.append(d)
   if d*d!=n:ans.append(n//d)
 return tuple(sorted(ans))

@lru_cache(None)
def self_options(s,x,c0,b0):
 ans=[]
 for c in range(c0,x,2):
  numerator=x*(x-c)
  if numerator%s==0:
   b=numerator//s
   if b>=b0 and b%2==0:ans.append((c,b))
 return tuple(ans)

@lru_cache(None)
def self_least(s,x,c0,b0):
 ans=self_options(s,x,c0,b0)
 return min(c+b for c,b in ans) if ans else None

def weak_cell(s,div,cword):
 step=lcm(div,2);allowance=BUDGET-(s-576);cap=480+allowance//2
 dp={0:0}
 for lo,c0,b0 in [(48,8,4)]*2+[(192,cword,64)]*2:
  vals=[]
  for x in range((lo+step-1)//step*step,lo+allowance//2+1,step):
   cost=self_least(s,x,c0,b0)
   if cost is not None:vals.append((x,cost))
  nd={}
  for total,cost in dp.items():
   for x,c in vals:
    if total+x<=cap and cost+c<nd.get(total+x,10**20):nd[total+x]=cost+c
  dp=nd
  if not dp:return {}
 return dp

label={i:[f'g{i}_{w}' for w in ('1','12','21','2')] for i in (1,2)}
C0={i:[[mass[label[i][r],label[i][t],label[i][2*(r//2)+t%2]] for t in range(4)] for r in range(4)] for i in (1,2)}
B0={i:[[mass[label[i][r],label[i][t],'Sigma'] for t in range(4)] for r in range(4)] for i in (1,2)}
checks={'divisor_rows':0,'weak_nonempty_rows':0,'weak_sum_pairs':0,'competitive_divisor_rows':0,'competitive_sum_pairs':0,'action_tuples':0,'self_admissible_action_tuples':0,'self_coefficient_tuples':0,'delta_divisors':0,'valid_full_cells':0}

def least_full_cell(i,s,theta,selfcap):
 opts=[self_options(s,theta[j],C0[i][j][j],B0[i][j][j]) for j in range(4)]
 if any(not z for z in opts):return None
 least=None
 for chosen in product(*opts):
  if sum(c+b for c,b in chosen)>selfcap:continue
  checks['self_coefficient_tuples']+=1
  u,y,x,ud=[r[0] for r in chosen]
  # Independent parametrization: choose the ad coefficient delta, not p.
  for delta in divisors(u*x):
   if delta%2 or delta<C0[i][0][3]:continue
   checks['delta_divisors']+=1
   p=u*x//delta
   if p%2 or p<C0[i][2][1] or (u*y)%p or (ud*p)%u:continue
   delta2=u*y//p;z=ud*p//u
   if delta2%2 or z%2:continue
   cm=[[u,u,x,delta],[y,y,z,ud],[u,p,x,x],[delta2,y,ud,ud]]
   cost=0;valid=True
   for r in range(4):
    for t in range(4):
     c=cm[r][t];output=2*(r//2)+t%2
     numerator=theta[r]*theta[t]-c*theta[output]
     if c<C0[i][r][t] or c%2 or numerator%s:
      valid=False;break
     bottom=numerator//s
     if bottom<B0[i][r][t] or bottom%2:
      valid=False;break
     cost+=c+bottom
    if not valid:break
   if valid:
    checks['valid_full_cells']+=1
    candidate={'cost':cost,'theta':list(theta),'u_x_y_z_p':[u,x,y,z,p]}
    if least is None or cost<least['cost']:least=candidate
 return least

def strong_cell(i,s,div,limits):
 step=lcm(div,2);result={}
 for A,selfcap in limits.items():
  firstgen=(48+step-1)//step*step;firstword=(192+step-1)//step*step
  for ga in range(firstgen,A-48-384+1,step):
   for gd in range(firstgen,A-ga-384+1,step):
    for wb in range(firstword,A-ga-gd-192+1,step):
     wc=A-ga-gd-wb
     if wc<192 or wc%step:continue
     checks['action_tuples']+=1;theta=(ga,wb,wc,gd)
     costs=[self_least(s,theta[j],C0[i][j][j],B0[i][j][j]) for j in range(4)]
     if None in costs or sum(costs)>selfcap:continue
     checks['self_admissible_action_tuples']+=1
     cand=least_full_cell(i,s,theta,selfcap)
     if cand is not None and (A not in result or cand['cost']<result[A]['cost']):result[A]=cand
 return result

minimum=None;min_rows=[];surviving_weak=[]
for s in range(576,576+BUDGET+1,4):
 cache={}
 for a in divisors(2*s):
  b=2*s//a;checks['divisor_rows']+=1
  for key in [(a,8),(b,16)]:
   if key not in cache:cache[key]=weak_cell(s,*key)
  one,two=cache[a,8],cache[b,16]
  if not one or not two:continue
  checks['weak_nonempty_rows']+=1
  limits1={};limits2={};pairs=[]
  for A,e1 in one.items():
   for B,e2 in two.items():
    checks['weak_sum_pairs']+=1
    assert (2*A*B)%s==0
    base=s+2*(A+B)+2*A*B//s+776
    if base+e1+e2<=MASS_CAP:
     pairs.append((A,B));limits1[A]=max(limits1.get(A,0),MASS_CAP-base-e2);limits2[B]=max(limits2.get(B,0),MASS_CAP-base-e1)
  if not pairs:continue
  checks['competitive_divisor_rows']+=1;checks['competitive_sum_pairs']+=len(pairs)
  left=strong_cell(1,s,a,limits1);right=strong_cell(2,s,b,limits2)
  surviving_weak.append([s,a,b,len(pairs),len(left),len(right)])
  for A,B in pairs:
   if A not in left or B not in right:continue
   total=s+2*(A+B)+2*A*B//s+left[A]['cost']+right[B]['cost']
   if minimum is None or total<minimum:minimum=total;min_rows=[]
   if total==minimum:min_rows.append({'s':s,'a':a,'b':b,'A':A,'B':B,'cell1':left[A],'cell2':right[B],'total':total})
   assert total>MASS_CAP
assert minimum==5544 and (minimum-4424)//2==560

# Independent full multiplication-table verification for the scalar attainer.
basis=['mu','Sigma']+names;tab={}
for b in basis:tab['mu',b,b]=1;tab[b,'mu',b]=1
tab['Sigma','Sigma','Sigma']=648
th={b:(72 if b.endswith(('_1','_2')) else 216) for b in names}
for b in names:tab['Sigma',b,'Sigma']=th[b];tab[b,'Sigma','Sigma']=th[b]
cm=[[18,18,18,6],[18,18,54,18],[18,54,18,18],[6,18,18,18]]
for i in (1,2):
 for r,t in product(range(4),repeat=2):
  a,b=label[i][r],label[i][t];z=label[i][2*(r//2)+t%2];c=cm[r][t]
  tab[a,b,z]=c;num=th[a]*th[b]-c*th[z];assert num%648==0;tab[a,b,'Sigma']=num//648
for i,j in ((1,2),(2,1)):
 for a,b in product(label[i],label[j]):assert th[a]*th[b]%648==0;tab[a,b,'Sigma']=th[a]*th[b]//648
assert set(tab)==set(trace) and len(tab)==132
for key,c in tab.items():assert c>0 and c>=mass[key] and (c-sum(trace[key].values()))%2==0
products={(a,b):{z:c for (aa,bb,z),c in tab.items() if aa==a and bb==b} for a,b in product(basis,repeat=2)}
for a,b,c in product(basis,repeat=3):
 left=defaultdict(int);right=defaultdict(int)
 for j,vv in products[a,b].items():
  for k,ww in products[j,c].items():left[k]+=vv*ww
 for j,vv in products[b,c].items():
  for k,ww in products[a,j].items():right[k]+=vv*ww
 assert dict(left)==dict(right)
assert sum(tab.values())==5563 and sum(v for (a,b,z),v in tab.items() if 'mu' not in (a,b))==5544
out={'excluded_pair_budget':559,'excluded_mass_budget':MASS_CAP,'S_range':[576,1692,4],'proved_pair_lower_bound':560,'minimum_relaxation_mass':minimum,'counts':checks,'minimum_rows':min_rows,'weak_survivor_rows':surviving_weak,'scalar_attainer_positions':132,'scalar_attainer_associativity_triples':1000,'scope':'Exact optimum560 of the stated integer ordinary-dimension relaxation. Therefore every original132-support Laurent lift costs>=560,but no Laurent lift at560 or all810-position bound is asserted.'}
Path('work/gct/support132_full_scalar_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('minimum_rows','weak_survivor_rows')},indent=2))
