"""Find finite-field ordinary quartics and certify a nondegenerate KS cup form.
All arithmetic is exact. The residue computation is described in the companion
note; it computes the Serre-dual normal boundary, not a Hasse derivative.
"""
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
from random import Random
from time import perf_counter
import json
import sympy as S

base=Path(__file__).resolve().parents[1]
z0,z1,z2,u,v,x,y=S.symbols('z0 z1 z2 u v x y')
mon4=[(a,b,4-a-b)for a in range(5)for b in range(5-a)]
quad=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
a_basis=[(2,1,1),(1,2,1),(1,1,2)]

def terms(expr,vs,p):
 return {m:int(c)%p for m,c in S.Poly(expr,*vs,modulus=p).terms()if int(c)%p}
def solve(mat,rhs,p):
 a=[[int(c)%p for c in row]+[int(b)%p]for row,b in zip(mat,rhs)]
 n=len(mat[0]); piv=[]; r=0
 for c in range(n):
  k=next((k for k in range(r,len(a))if a[k][c]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];inv=pow(a[r][c],-1,p);a[r]=[(q*inv)%p for q in a[r]]
  for k in range(len(a)):
   if k!=r and a[k][c]:
    h=a[k][c];a[k]=[(aa-h*bb)%p for aa,bb in zip(a[k],a[r])]
  piv.append(c);r+=1
  if r==len(a):break
 if any(not any(row[:n])and row[n]for row in a):return None,piv
 sol=[0]*n
 for rr,c in enumerate(piv):sol[c]=a[rr][-1]
 return sol,piv

def degree_mons(d):return [(i,j)for i in range(d+1)for j in range(d+1-i)]
def bezout_one(f,p):
 fs=[terms(f,(u,v),p),terms(S.diff(f,u),(u,v),p),terms(S.diff(f,v),(u,v),p)]
 for D in range(4,13):
  rows=degree_mons(D);ri={m:i for i,m in enumerate(rows)}
  cs=[(h,m)for h,d in enumerate([4,3,3])for m in degree_mons(D-d)]
  mat=[[0]*len(cs)for _ in rows]
  for j,(h,m)in enumerate(cs):
   for e,c in fs[h].items():mat[ri[(e[0]+m[0],e[1]+m[1])]][j]=c
  rhs=[int(m==(0,0))for m in rows];sol,_=solve(mat,rhs,p)
  if sol is not None:
   polys=[{}for _ in range(3)]
   for coeff,(h,m)in zip(sol,cs):
    if coeff:polys[h][m]=coeff
   es=[sum(c*u**i*v**j for(i,j),c in po.items())for po in polys]
   ident=S.Poly(es[0]*f+es[1]*S.diff(f,u)+es[2]*S.diff(f,v)-1,u,v,modulus=p).is_zero
   assert ident
   return polys,es,D
 raise RuntimeError('Bezout degree bound exceeded')

class Algebra:
 def __init__(self,f0,p):
  self.p=p; pol=S.Poly(f0,y,modulus=p);lc=int(pol.LC())%p
  self.mod=[int(pol.nth(i))*pow(lc,-1,p)%p for i in range(4)]
  self.zero=(0,0,0,0);self.one=(1,0,0,0);self.Y=(0,1,0,0)
 def add(self,a,b):return tuple((a[i]+b[i])%self.p for i in range(4))
 def neg(self,a):return tuple(-c%self.p for c in a)
 def scale(self,c,a):return tuple(c*q%self.p for q in a)
 def mul(self,a,b):
  c=[0]*7
  for i in range(4):
   for j in range(4):c[i+j]=(c[i+j]+a[i]*b[j])%self.p
  for n in range(6,3,-1):
   for j in range(4):c[n-4+j]=(c[n-4+j]-c[n]*self.mod[j])%self.p
  return tuple(c[:4])
 def inv(self,a):
  cols=[self.mul(a,tuple(int(i==j)for i in range(4)))for j in range(4)]
  sol,_=solve([[cols[j][i]for j in range(4)]for i in range(4)],[1,0,0,0],self.p)
  assert sol is not None
  return tuple(sol)
 def trace(self,a):
  return sum(self.mul(a,tuple(int(i==j)for i in range(4)))[j]for j in range(4))%self.p

def cup_matrix(F,p):
 f1=S.expand(F.subs({z0:u,z1:1,z2:v}));polys,es,D=bezout_one(f1,p)
 f=S.expand(F.subs({z0:1,z1:x,z2:y}));f0=f.subs(x,0)
 B=Algebra(f0,p);zero=B.zero;one=B.one;N=D+4
 def smul(a,b):
  out=[zero]*(N+1)
  for i,aa in enumerate(a):
   if aa==zero:continue
   for j,bb in enumerate(b[:N+1-i]):
    if bb!=zero:out[i+j]=B.add(out[i+j],B.mul(aa,bb))
  return out
 def spow(a,n):
  r=[one]+[zero]*N
  for _ in range(n):r=smul(r,a)
  return r
 def ev(poly,ys):
  out=[zero]*(N+1)
  cache={j:spow(ys,j)for j in {e[1]for e in poly}}
  for(i,j),c in poly.items():
   for n in range(N+1-i):out[n+i]=B.add(out[n+i],B.scale(c,cache[j][n]))
  return out
 ft=terms(f,(x,y),p);fyt=terms(S.diff(f,y),(x,y),p)
 ys=[B.Y]+[zero]*N;fy0=ev(fyt,ys)[0];fy0inv=B.inv(fy0)
 for n in range(1,N+1):
  res=ev(ft,ys)[n];ys[n]=B.neg(B.mul(fy0inv,res))
 assert all(c==zero for c in ev(ft,ys))
 fys=ev(fyt,ys);inv=[fy0inv]+[zero]*N
 for n in range(1,N+1):
  acc=zero
  for i in range(1,n+1):acc=B.add(acc,B.mul(fys[i],inv[n-i]))
  inv[n]=B.neg(B.mul(fy0inv,acc))
 assert smul(fys,inv)==[one]+[zero]*N
 inv2=smul(inv,inv)
 maxpow=max((j for i,j in polys[1]),default=0)+6
 ratios={e:smul(spow(ys,e),inv2)for e in range(maxpow+1)}
 mat=[]
 for qa,qb,qc in quad:
  row=[]
  for ha,hb,hc in mon4:
   acc=zero
   for(i,j),c in polys[1].items():
    n=i+j+ha+hc-qb-3
    if 0<=n<=N:acc=B.add(acc,B.scale(-c,ratios[j+hc+qc][n]))
   row.append(B.trace(acc))
  mat.append(row)
 sol,piv=solve(mat,[1,0,0,1,0,1],p)
 rank=len(piv)
 assert rank==6,(p,rank,F,mat)
 assert sol is not None
 H=sum(c*z0**a*z1**b*z2**cc for c,(a,b,cc)in zip(sol,mon4))
 result=[sum(row[j]*sol[j]for j in range(15))%p for row in mat]
 assert result==[1,0,0,1,0,1]
 def vector(poly):
  td=terms(poly,(z0,z1,z2),p)
  return [td.get(m,0)for m in mon4]
 kernel_checks=[]
 for name,poly in [('F',F)]+[(str(zj)+'*dF/d'+str(zi),zj*S.diff(F,zi))for zi in [z0,z1,z2]for zj in [z0,z1,z2]]:
  vv=vector(poly);im=[sum(row[j]*vv[j]for j in range(15))%p for row in mat]
  kernel_checks.append({'normal_trivial_direction':name,'cup_coordinates':im})
 assert all(not any(c['cup_coordinates'])for c in kernel_checks)
 return {'F':str(F),'H':str(H),'KS_cup_matrix':[[1,0,0],[0,1,0],[0,0,1]],'normal_boundary_dual_6_by_15':mat,'normal_boundary_rank':rank,'Bezout_degree_bound':D,'Bezout_R_A_B':[str(e)for e in es],'Bezout_identity_verified':True,'residue_algebra_modulus':str(f0),'implicit_series_checked_through_degree':N,'monomial_order':mon4,'quadratic_order':quad,'H_coefficients':sol,'trivial_deformation_kernel_checks':kernel_checks}

def hasse(F,p):
 d=terms(S.expand(F**(p-1)),(z0,z1,z2),p)
 return [[d.get(tuple(p*a[i]-b[i]for i in range(3)),0)for b in a_basis]for a in a_basis]
def smooth(F,p):
 out=[]
 for i,z in enumerate([z0,z1,z2]):
  vs=[v for v in [z0,z1,z2]if v!=z]
  pols=[e.subs(z,1)for e in [F,S.diff(F,z0),S.diff(F,z1),S.diff(F,z2)]]
  g=S.groebner(pols,*vs,modulus=p)
  out.append(len(g.polys)==1 and g.polys[0].as_expr()==1)
 return out

start=perf_counter();report={'started_utc':datetime.now(timezone.utc).isoformat(),'method':'Normal-boundary Cech lift plus Serre residue trace. Matrix is defined up to a common nonzero normalization scalar; nonsingularity is exact.','pairs':[]}
for p in [2,3]:
 rng=Random(6303+p);found=None
 for attempt in range(1,5001):
  co=[rng.randrange(p)for _ in mon4];co[mon4.index((0,0,4))]=1
  F=sum(c*z0**a*z1**b*z2**cc for c,(a,b,cc)in zip(co,mon4))
  f0=S.Poly(F.subs({z0:1,z1:0,z2:y}),y,modulus=p)
  if S.gcd(f0,f0.diff()).degree()!=0:continue
  hw=hasse(F,p)
  if int(S.Matrix(hw).det())%p==0:continue
  sm=smooth(F,p)
  if not all(sm):continue
  t=perf_counter();pair=cup_matrix(F,p)
  pair.update(p=p,attempt=attempt,F_coefficients=co,Hasse_Witt=hw,Hasse_determinant=int(S.Matrix(hw).det())%p,smooth_chart_Groebner_unit_ideals=sm,residue_fibre_separable=True,runtime_seconds=perf_counter()-t)
  report['pairs'].append(pair);found=pair;print('found p',p,'attempt',attempt,'F',F,'H',pair['H'],flush=True);break
 assert found is not None
# Independent calibration: the Fermat-five form from certified C.3bf.
p=5;F=z0**4+z1**4+z2**4;cal=cup_matrix(F,p);cal['p']=p
knownH=z0**2*z1**2+z0**2*z2**2+z1**2*z2**2
vv=terms(knownH,(z0,z1,z2),p)
known=[sum(row[j]*vv.get(mon4[j],0)for j in range(15))%p for row in cal['normal_boundary_dual_6_by_15']]
assert known==[4,0,0,4,0,4]
cal['certified_bf_H_coordinates']=known
cal['certified_bf_expected_minus_identity']=True
report['fermat5_calibration']=cal
report['runtime_seconds']=perf_counter()-start
report['finished_utc']=datetime.now(timezone.utc).isoformat()
(base/'output'/'C3_small_characteristic_KS_pairs.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
