from pathlib import Path
from math import isqrt
from datetime import datetime,timezone
import json,hashlib
p=269;B=Path(__file__).parent

def pell(D):
 a0=isqrt(D);m=0;d=1;a=a0;hm2,hm1=0,1;km2,km1=1,0
 for step in range(100000):
  h,k=a*hm1+hm2,a*km1+km2;n=h*h-D*k*k
  if abs(n)==1:return h,k,n,step+1
  hm2,hm1=hm1,h;km2,km1=km1,k
  m=d*a-m;d=(D-m*m)//d;a=(a0+m)//d
 raise RuntimeError('No finite Pell candidate found')

def mul(x,y,D,mod):return ((x[0]*y[0]+D*x[1]*y[1])%mod,(x[0]*y[1]+x[1]*y[0])%mod)
def power(x,n,D,mod):
 out=(1,0)
 while n:
  if n&1:out=mul(out,x,D,mod)
  x=mul(x,x,D,mod);n//=2
 return out
rows=[]
for label,r0,D0 in [('chi_-4',-1,3),('chi_8',2,2),('chi_-8',-2,6)]:
 for nu in [0,1]:
  r=r0*p**nu;D=D0*p**nu;a,b,n,steps=pell(D);assert a*a-D*b*b==n and abs(n)==1
  row={'label':label,'effective_residue':267 if nu==0 else 133,'quadratic_radicand':r,'real_quadratic_radicand':D,'unit':[a,b],'norm':n,'monic_annihilator':[1,-2*a,n],'pell_search_steps':steps}
  discs=[]
  for dd in [-3,r,-3*r]:
   while any(dd%(q*q)==0 for q in range(2,isqrt(abs(dd))+1)):
    q=next(q for q in range(2,isqrt(abs(dd))+1) if dd%(q*q)==0);dd//=q*q
   disc=dd if dd%4==1 else 4*dd;assert abs(disc)<=6456;discs.append(disc)
  row['quadratic_fundamental_discriminants']=discs
  if nu==0:
   mod=p*p;q=p*p-1;val=power((a,b),q,D,mod);assert val[0]==1 and val[1]%p==0
   fermat=(val[1]//p)%p;assert fermat
   projected=power((a,b),2*q,D,mod);assert projected==(1,(2*p*fermat)%mod)
   row.update(local_absolute_ramification=1,unit_power_exponent=q,unit_power_mod_p2=list(val),projected_unit_power_mod_p2=list(projected),nonzero_fermat_coefficient=fermat)
  else:
   assert a%p and b%p
   log=(b*pow(a,-1,p))%p;assert log
   row.update(local_absolute_ramification=2,linear_log_coefficient=log,projected_linear_log_coefficient=2*log%p)
  rows.append(row)
count=sum(53//n for n in range(1,54));assert count<269 and 4*6456<9*54**2
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_FINITE_ONLY','p':p,'quadratic_Minkowski_representative_norm_max':53,'quadratic_ideal_count_bound':count,'integer_bound':[4*6456,9*54**2],'rows':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact six Pell units, all displayed quadratic discriminants, finite ideal-count bound and p-local nonzero unit witnesses only; no whole strict or common-window theorem claimed.'}
(B/'quadratic_units_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
