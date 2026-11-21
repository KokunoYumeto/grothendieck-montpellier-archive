"""G034 complete fixed positive formula on the outer-five one-twist wall."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from itertools import product,combinations
from math import comb,prod
import sys,json,argparse
HERE=Path(__file__).resolve().parent
sys.path.append(str(HERE.parent/'theta'/'outer5'))
sys.path.append(str(HERE.parent/'theta'/'outer5'/'variable_wall'))
import first_power_zero_twist_positive as first
import second_power_zero_twist_positive as second
import third_power_fixed_twist_positive as third
import five_point_two_row_positive as bulk
import two_row_positive as one_below
import two_below_all_positive as two_below
import three_below_all_positive as three_below
import positive_one_twist_chamber as upper
import one_twist_strip as strip
LABELS=upper.LABELS
SIZES=upper.SIZES
CHAR=upper.CHAR
PERIODS=(1,2,2,3,6,4,5)
RAW={key:json.loads((HERE/name).read_text()) for key,name in
     [('A','ONE_TWIST_TRIPLE_A_CHECK.json'),('B','ONE_TWIST_TRIPLE_B_CHECK.json')]}
POLYS={key:[{tuple(map(int,phase.split(','))):tuple((tuple(map(int,e.split(','))),Fraction(*v)) for e,v in poly.items()) for phase,poly in row.items()} for row in data['phase_polynomials']] for key,data in RAW.items()}
ORDERS={key:((0,0,0),)+tuple(map(tuple,data['active_orders'])) for key,data in RAW.items()}

def transpose(mu):return tuple(sum(x>=i for x in mu) for i in range(1,max(mu)+1))

@lru_cache(None)
def cone_traces(branch,parameters):
 out=[]
 for L,row in zip(PERIODS,POLYS[branch]):
  poly=row[tuple(x%L for x in parameters)]
  value=sum(c*prod(x**p for x,p in zip(parameters,e)) for e,c in poly)
  assert value.denominator==1
  out.append(value.numerator)
 return tuple(out)

@lru_cache(None)
def cone_value(branch,label,parameters):
 numerator=sum(s*c*t for s,c,t in zip(SIZES,CHAR[LABELS.index(label)],cone_traces(branch,parameters)))
 assert numerator%120==0
 return numerator//120

@lru_cache(None)
def cone_constant(branch,label,residue,order):
 value=0
 for steps in product(*(range(i+1) for i in order)):
  c=(-1)**(sum(order)-sum(steps))*prod(comb(i,j) for i,j in zip(order,steps))
  value+=c*cone_value(branch,label,tuple(r+60*j for r,j in zip(residue,steps)))
 assert value>=0,(branch,label,residue,order,value)
 return value

def route(x,b,k,d,mu):
 if any(type(v)is not int or v<0 for v in (x,b,k,d)):
  raise ValueError('x,b,k,d must be nonnegative integers')
 mu=tuple(mu)
 if mu not in LABELS:raise ValueError('outer must partition five')
 if 2*b+x+3<5*k:raise ValueError('require 2b+x+3>=5k')
 label=''.join(map(str,mu))
 if k==0:return 'bulk',(x,b,0,1,d,mu)
 if k==1:return 'one_below',('below',x,b,1,d,mu)
 if k==2:return 'three_below',(x,b,2,d,mu)
 if k==3:return 'third',(x,b,1,d,label)
 if b<=2*k+1:
  H=d+3*b+2*x+4-5*k
  nu=transpose(mu) if H%2 else mu
  xp=2*b+x+3-5*k;kp=max(0,b+1-k)
  if b<=2*k-2:return 'bulk',(xp,1,kp,b-2*kp,0,nu)
  defect=b-2*k+2
  if defect==1:return 'one_below',('below',xp,1,kp,0,nu)
  if defect==2:return 'two_below',(xp,1,kp,0,nu)
  return 'three_below',(xp,1,kp,0,nu)
 if b>=3*k-3:return 'upper',(x,b,k,d,mu)
 if b==3*k-4:return 'strip',(x,k,d,mu)
 t=3*k-5-b
 effective=transpose(mu) if (d+b+x+1)%2 else mu
 if x>=t:
  parameters=(x-t,t,k-t-7)
  assert min(parameters)>=0
  return 'A',(effective,parameters)
 parameters=(x,t-x-1,2*b+x+3-5*k)
 assert min(parameters)>=0
 return 'B',(effective,parameters)

def cone_tags(branch,label,parameters):
 residue=tuple(x%60 for x in parameters);quotient=tuple(x//60 for x in parameters)
 return [dict(branch=branch,label=label,parameters=parameters,residue=residue,quotient=quotient,order=o,constant=cone_constant(branch,label,residue,o)) for o in ORDERS[branch]]

MODULES={'bulk':bulk,'first':first,'second':second,'third':third,'one_below':one_below,'two_below':two_below,'three_below':three_below,'upper':upper,'strip':strip}
def coefficient(x,b,k,d=0,mu=(5,)):
 branch,args=route(x,b,k,d,mu)
 if branch in MODULES:return MODULES[branch].coefficient(*args)
 return sum(t['constant']*prod(comb(q,j) if q>=j else 0 for q,j in zip(t['quotient'],t['order'])) for t in cone_tags(branch,*args))

def polytopes(x,b,k,d=0,mu=(5,)):
 branch,args=route(x,b,k,d,mu)
 if branch in ('bulk','first','second','third','strip'):
  return {'branch':branch,'mapped_parameters':args,'polytopes':MODULES[branch].polytopes(*args)}
 if branch in ('one_below','two_below','three_below'):
  tags=MODULES[branch].polytope_tags(*args)
  return {'branch':branch,'mapped_parameters':args,'polytopes':[one_below.constraints(t) for t in tags if t.get('constant',1)]}
 if branch=='upper':tags=upper.tags(*args)
 else:tags=cone_tags(branch,*args)
 return {'branch':branch,'mapped_parameters':args,'polytopes':[upper.constraints(t) for t in tags if t['constant']]}

def partition_route(lam,mu=(5,)):
 lam=tuple(lam);mu=tuple(mu)
 if any(type(v)is not int or v<0 for v in lam) or any(lam[i]<lam[i+1] for i in range(len(lam)-1)):
  raise ValueError('lambda must be a nonnegative partition')
 while lam and lam[-1]==0:lam=lam[:-1]
 if sum(lam)%5:raise ValueError('partition size must be divisible by five')
 if mu not in LABELS:raise ValueError('outer must partition five')
 n=sum(lam)//5
 if len(lam)>5:return {'zero':'more than five rows','inner':n}
 lam=lam+(0,)*(5-len(lam));original=lam
 complement=False
 if lam[1]!=lam[2]+1:
  if lam[2]!=lam[3]+1:raise ValueError('require lambda2=lambda3+1 or lambda3=lambda4+1')
  H=lam[0];lam=tuple(H-v for v in reversed(lam));n=H-n
  if H%2:mu=transpose(mu)
  complement=True
 e=max(0,n-lam[1]);n0=n-e
 normalized=(lam[0]-5*e,)+lam[1:]
 d=lam[4];x=lam[3]-lam[4];b=lam[2]-lam[3];k=lam[1]-n0
 assert normalized==(d+3*b+2*x+4-5*k,d+b+x+1,d+b+x,d+x,d)
 return {'original':original,'complement':complement,'stable_power':e,'normalized':normalized,'parameters':(x,b,k,d,mu),'selected':route(x,b,k,d,mu)}

def coefficient_partition(lam,mu=(5,)):
 r=partition_route(lam,mu)
 return 0 if 'zero' in r else coefficient(*r['parameters'])

def partition_polytopes(lam,mu=(5,)):
 r=partition_route(lam,mu)
 return {'route':r,'formula':{'polytopes':[]} if 'zero' in r else polytopes(*r['parameters'])}

def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('x','b','k'):p.add_argument('--'+name,type=int)
 p.add_argument('--partition',type=int,nargs='+')
 p.add_argument('--d',type=int,default=0);p.add_argument('--outer',default='5');p.add_argument('--polytopes',action='store_true')
 a=p.parse_args();mu=tuple(map(int,a.outer.split(',')))
 if a.partition is not None:
  result={'coefficient':coefficient_partition(a.partition,mu),'route':partition_route(a.partition,mu)}
  if a.polytopes:result['positive_formula']=partition_polytopes(a.partition,mu)
  print(json.dumps(result,indent=2));return
 if any(v is None for v in (a.x,a.b,a.k)):p.error('supply --partition or all of --x,--b,--k')
 result={'inner':a.d+a.b+a.x+1-a.k,'output':[a.d+3*a.b+2*a.x+4-5*a.k,a.d+a.b+a.x+1,a.d+a.b+a.x,a.d+a.x,a.d],
         'coefficient':coefficient(a.x,a.b,a.k,a.d,mu),'route':route(a.x,a.b,a.k,a.d,mu)}
 if a.polytopes:result['positive_formula']=polytopes(a.x,a.b,a.k,a.d,mu)
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
