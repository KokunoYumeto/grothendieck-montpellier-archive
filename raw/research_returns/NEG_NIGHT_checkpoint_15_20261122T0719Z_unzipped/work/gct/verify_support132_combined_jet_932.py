"""Independent exact integer certificate: original132-support lifts cost>=932.
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

PAIR_CAP=931;BUDGET=2*PAIR_CAP;MASS_CAP=4424+BUDGET
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
# Direct verification of every mod2 order used in the factor obstruction.
def reduction_order(key):
 pp=sp.Poly(sum((c%2)*q**(j+64) for j,c in trace[key].items()),q,modulus=2)
 assert not pp.is_zero
 fac=sp.Poly(q+1,q,modulus=2);order=0
 while int(pp.eval(1))%2==0:pp=pp.exquo(fac);order+=1
 return order
for i in (1,2):
 aa,bb,cc,dd=label[i]
 positions=[(aa,aa,aa),(dd,dd,dd),(cc,cc,cc),(bb,bb,bb),(aa,dd,bb),(dd,aa,cc),(cc,bb,dd),(bb,cc,aa)]
 orders=[reduction_order(key) for key in positions]
 assert orders==([4,4,4,4,2,2,6,6] if i==1 else [4,4,6,6,2,2,8,8])


# Exact source polynomials and their complete factorizations, independently
# checked before generating finite divisor statistics for saturated factors.
phi2=q+1;phi3=q*q+q+1;phi4=q*q+1;phi6=q*q-q+1;phi8=q**4+1
quartic=q**4+2*q**3+2*q+1;psi=D*(D-3);K=D-2
factor_data={
 'gen':(psi*K,[(phi2,2),(phi6,1),(phi4,1)]),
 'delta':(psi,[(phi2,2),(phi6,1)]),
 'word1':(psi*K,[(phi2,2),(phi6,1),(phi4,1)]),
 'word2':(psi*K*K,[(phi2,2),(phi6,1),(phi4,2)]),
 'pair1':(psi*(D*D-2*D-2),[(phi2,2),(phi6,1),(quartic,1)]),
 'pair2':(C*(q*q+q**-2)**2,[(phi3,1),(phi8,2)])}
fixed_data={}
def poly_order(f):
 pp=sp.Poly(sp.expand(f),q,modulus=2)
 assert not pp.is_zero
 linear=sp.Poly(q+1,q,modulus=2);r=0
 while int(pp.eval(1))%2==0:pp=pp.exquo(linear);r+=1
 return r
for role,(f,factors) in factor_data.items():
 numerator=sp.prod(fac**mult for fac,mult in factors)
 # Reciprocal source polynomials have the indicated monomial denominator.
 degree=sp.degree(numerator,q);assert degree%2==0
 assert sp.expand(f*q**(degree//2)-numerator)==0
 assert all(sp.Poly(fac,q).LC()==1 and sp.Poly(fac,q).TC()==1 for fac,mult in factors)
 choices={(1,0)}
 for fac,mult in factors:
  value=fac.subs(q,1);assert value.is_Integer and value>0
  order=poly_order(fac)
  choices={(value**j*a,order*j+b) for a,b in choices for j in range(mult+1)}
 minimum=f.subs(q,1);assert minimum.is_Integer
 fixed_data[role]=(int(minimum),tuple((int(a),b) for a,b in sorted(choices)))
for i in (1,2):
 aa,bb,cc,dd=label[i]
 rolekeys=[('gen',(aa,aa,aa)),('gen',(dd,dd,dd)),('word'+str(i),(bb,bb,bb)),('word'+str(i),(cc,cc,cc)),('delta',(aa,dd,bb)),('delta',(dd,aa,cc)),('pair'+str(i),(bb,cc,aa)),('pair'+str(i),(cc,bb,dd))]
 for role,key in rolekeys:
  source_absolute=sum(abs(c)*q**j for j,c in trace[key].items())
  assert sp.expand(source_absolute-factor_data[role][0])==0
  assert mass[key]==fixed_data[role][0]

@lru_cache(maxsize=1000000)
def saturated_identity(i,u,x,delta,p):
 # Any one of the four saturated factors can be the fixed factor F.
 values=(u,x,delta,p);roles=('gen','word'+str(i),'delta','pair'+str(i))
 orders=(4,4 if i==1 else 6,2,6 if i==1 else 8)
 for k in range(4):
  lower,choices=fixed_data[roles[k]]
  if values[k]!=lower:continue
  mate=k^1
  cindex,dindex=(2,3) if k<2 else (0,1)
  possible=False
  for g,rg in choices:
   if values[cindex]%g:continue
   h=values[cindex]//g
   if values[mate]%h:continue
   j=values[mate]//h
   rh=orders[cindex]-rg;rj=orders[mate]-rh
   if min(rh,rj)<0:continue
   if (lower//g)*j!=values[dindex]:continue
   if orders[k]-rg+rj!=orders[dindex]:continue
   if (h%2==1)!=(rh==0) or (j%2==1)!=(rj==0):continue
   possible=True;break
  if not possible:return False
 return True


# Exact source interface for all four bottom-saturation orientations.
for i in (1,2):
 for g,w,ar,br in [(0,1,0,1),(0,2,2,0),(3,2,3,2),(3,1,1,3)]:
  gg,ww=label[i][g],label[i][w];left,right=label[i][ar],label[i][br]
  assert sp.expand(sum(abs(c)*q**j for j,c in trace[gg,gg,'Sigma'].items())-D)==0
  assert sp.expand(sum(abs(c)*q**j for j,c in trace[left,right,'Sigma'].items())-D**2)==0
  assert parity_equal(('Sigma',gg,'Sigma'),0 if i==1 else D**2*C)
  assert parity_equal((gg,gg,gg),D**2*C)
  assert parity_equal((ww,ww,ww),D**(2 if i==1 else 3)*C)
  assert parity_equal((ww,ww,'Sigma'),D**2)

# Independent exact interfaces for the two additional grading obstructions.
pair_floor=factor_data['pair2'][0]
assert sp.simplify(pair_floor.subs(q,sp.I))==4
assert sp.simplify(sp.diff(pair_floor,q).subs(q,sp.I))==8
assert sp.expand(sum(abs(co)*q**j for j,co in trace['Sigma','Sigma','Sigma'].items())-4*D**2*C**2)==0
for gen1 in ('g1_1','g1_2'):
 assert sp.expand(sum(abs(co)*q**j for j,co in trace[gen1,gen1,gen1].items())-psi*(D-2))==0
 assert sp.expand(sum(abs(co)*q**j for j,co in trace[gen1,gen1,'Sigma'].items())-D)==0
 for gen2 in ('g2_1','g2_2'):
  assert parity_equal(('Sigma',gen2,'Sigma'),D**2*C)
  assert parity_equal((gen1,gen2,'Sigma'),D)
assert sp.simplify((4*D**2*C**2).subs(q,sp.I))==16
assert sp.simplify((psi*(D-2)).subs(q,sp.I))==0
assert sp.simplify((D*C).subs(q,sp.I))==2

checks={'divisor_rows':0,'weak_nonempty_rows':0,'weak_sum_pairs':0,'competitive_divisor_rows':0,'competitive_sum_pairs':0,'action_tuples':0,'self_admissible_action_tuples':0,'self_coefficient_tuples':0,'delta_divisors':0,'valid_full_cells':0,'character_filter_rejections':0,'saturated_factor_rejections':0,'bottom_saturation_rejections':0,'double_root_rejections':0,'bottom_square_rejections':0}

def least_full_cell(i,s,theta,selfcap):
 opts=[self_options(s,theta[j],C0[i][j][j],B0[i][j][j]) for j in range(4)]
 if any(not z for z in opts):return None
 least=None
 for chosen in product(*opts):
  if sum(c+b for c,b in chosen)>selfcap:continue
  checks['self_coefficient_tuples']+=1
  u,y,x,ud=[r[0] for r in chosen]
  if i==1 and s==576 and any(chosen[j][0]==8 and chosen[j][1]%4!=2 for j in (0,3)):
   checks['bottom_square_rejections']+=1;continue
  if not ((u%4==0 and ud%4==0) or (x%4==0 and y%4==0)):
   checks['character_filter_rejections']+=1;continue
  # Independent parametrization: choose the ad coefficient delta, not p.
  for delta in divisors(u*x):
   if delta%2 or delta<C0[i][0][3]:continue
   checks['delta_divisors']+=1
   p=u*x//delta
   if p%2 or p<C0[i][2][1] or (u*y)%p or (ud*p)%u:continue
   delta2=u*y//p;z=ud*p//u
   if delta2%2 or z%2 or delta2<C0[i][3][0] or z<C0[i][1][2]:continue
   if i==2 and any(word==16 and dd%4==0 and pair<20 for word,dd,pair in [(x,delta,p),(y,delta2,p),(x,delta,z),(y,delta2,z)]):
    checks['double_root_rejections']+=1;continue
   if not all(saturated_identity(i,*v) for v in [(u,x,delta,p),(u,y,delta2,p),(ud,x,delta,z),(ud,y,delta2,z)]):
    checks['saturated_factor_rejections']+=1;continue
   cm=[[u,u,x,delta],[y,y,z,ud],[u,p,x,x],[delta2,y,ud,ud]]
   cost=0;valid=True;bm=[[None]*4 for _ in range(4)]
   for r in range(4):
    for t in range(4):
     c=cm[r][t];output=2*(r//2)+t%2
     numerator=theta[r]*theta[t]-c*theta[output]
     if c<C0[i][r][t] or c%2 or numerator%s:
      valid=False;break
     bottom=numerator//s
     if bottom<B0[i][r][t] or bottom%2:
      valid=False;break
     bm[r][t]=bottom
     cost+=c+bottom
    if not valid:break
   if valid:
    for g,w,ar,br in [(0,1,0,1),(0,2,2,0),(3,2,3,2),(3,1,1,3)]:
     if bm[g][g]==4 and bm[ar][br]==16:
      residue=3*theta[g]+cm[g][g]-cm[w][w]
      if i==1:residue-=bm[w][w]-16
      if residue%4:
       checks['bottom_saturation_rejections']+=1;valid=False;break
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

assert minimum==6288 and (minimum-4424)//2==932

# Full scalar attainer; no Laurent lift is inferred.
basis=['mu','Sigma']+names;tab={}
for b in basis:tab['mu',b,b]=1;tab[b,'mu',b]=1
S=640;tab['Sigma','Sigma','Sigma']=S
th={b:((80 if b.endswith(('_1','_2')) else 240) if b.startswith('g1') else (96 if b.endswith(('_1','_2')) else 224)) for b in names}
for b in names:tab['Sigma',b,'Sigma']=th[b];tab[b,'Sigma','Sigma']=th[b]
parameters={1:(32,16,16,32,32),2:(16,24,24,16,16)}
for i in (1,2):
 u,x,y,z,p=parameters[i]
 assert (u*z)%p==0 and (u*x)%p==0 and (u*y)%p==0
 h=u*z//p;delta=u*x//p;delta2=u*y//p
 cm=[[u,u,x,delta],[y,y,z,h],[u,p,x,x],[delta2,y,h,h]]
 for r,t in product(range(4),repeat=2):
  a,b=label[i][r],label[i][t];out=label[i][2*(r//2)+t%2];c=cm[r][t]
  tab[a,b,out]=c;num=th[a]*th[b]-c*th[out]
  assert num%S==0;tab[a,b,'Sigma']=num//S
for i,j in ((1,2),(2,1)):
 for a,b in product(label[i],label[j]):
  assert th[a]*th[b]%S==0;tab[a,b,'Sigma']=th[a]*th[b]//S
assert set(tab)==set(trace) and len(tab)==132
for key,c in tab.items():assert c>0 and c>=mass[key] and (c-sum(trace[key].values()))%2==0
for i in (1,2):
 aa,bb,cc,dd=label[i];u,x,y,h=[tab[z,z,z] for z in (aa,cc,bb,dd)]
 assert (u%4==h%4==0) or (x%4==y%4==0)
 delta=tab[aa,dd,bb];delta2=tab[dd,aa,cc];p=tab[cc,bb,dd];z=tab[bb,cc,aa]
 assert all(saturated_identity(i,*v) for v in [(u,x,delta,p),(u,y,delta2,p),(h,x,delta,z),(h,y,delta2,z)])
 if i==2:assert all(not(word==16 and dd%4==0 and pair<20) for word,dd,pair in [(x,delta,p),(y,delta2,p),(x,delta,z),(y,delta2,z)])
 if i==1 and S==576:
  for gen in (aa,dd):assert tab[gen,gen,gen]!=8 or tab[gen,gen,'Sigma']%4==2
 for g,w,ar,br in [(0,1,0,1),(0,2,2,0),(3,2,3,2),(3,1,1,3)]:
  gg,ww=label[i][g],label[i][w];left,right=label[i][ar],label[i][br]
  if tab[gg,gg,'Sigma']==4 and tab[left,right,'Sigma']==16:
   residue=3*th[gg]+tab[gg,gg,gg]-tab[ww,ww,ww]
   if i==1:residue-=tab[ww,ww,'Sigma']-16
   assert residue%4==0
products={(a,b):{z:c for (aa,bb,z),c in tab.items() if aa==a and bb==b} for a,b in product(basis,repeat=2)}
for a,b,c in product(basis,repeat=3):
 left=defaultdict(int);right=defaultdict(int)
 for j,vv in products[a,b].items():
  for k,ww in products[j,c].items():left[k]+=vv*ww
 for j,vv in products[b,c].items():
  for k,ww in products[a,j].items():right[k]+=vv*ww
 assert dict(left)==dict(right)
assert sum(tab.values())==6307 and sum(v for (a,b,z),v in tab.items() if 'mu' not in (a,b))==6288
out={'excluded_pair_budget':PAIR_CAP,'excluded_mass_budget':MASS_CAP,'S_range':[576,2436,4],'proved_pair_lower_bound':932,'minimum_relaxation_mass':minimum,'counts':checks,'minimum_rows':min_rows,'weak_survivor_rows':surviving_weak,'scalar_attainer_positions':132,'scalar_attainer_associativity_triples':1000,'scope':'Exact optimum932 of the stated ordinary-dimension relaxation with the previous source and saturation filters plus double-root and saturated-bottom-square obstructions. Every original132-support integral Laurent lift costs>=932; no graded lift at932 or all810 bound is asserted.'}
Path('work/gct/support132_combined_jet_932_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('minimum_rows','weak_survivor_rows')},indent=2))
