"""G035 complete positive formula in normalized c<k, b+c>=2k."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from itertools import product,combinations
from math import comb,prod
import json,sys,argparse
HERE=Path(__file__).resolve().parent
sys.path.append(str(HERE.parent/'theta'/'outer5'/'variable_wall'))
import generic_twist_upper_positive as upper
import generic_twist_lower_positive as lower
import zero_twist_all_positive as zero
import one_twist_all_positive as one
LABELS=upper.LABELS;PERIODS=upper.PERIODS;CHAR=upper.CHAR;SIZES=upper.SIZES
NAMES=('D0','D1','D2','R1a','R1b','R2a','R2b','R3a','R3b')
RAW={name:json.loads((HERE/f'GENERIC_TWIST_BOUNDARY_{name}.json').read_text()) for name in NAMES}
POLYS={name:[{tuple(map(int,key.split(','))):tuple((tuple(map(int,e.split(','))),Fraction(*v)) for e,v in p.items()) for key,p in row.items()} for row in data['phase_polynomials']] for name,data in RAW.items()}
ORDERS={name:((0,)*data['dimension'],)+tuple(map(tuple,data['active_orders'])) for name,data in RAW.items()}

def boundary_physical(name,Z):
 if name.startswith('D'):
  D=int(name[1]);Y,T,C=Z;c=C+2;R=T+D+3
  return T+3-D+Y,c+2*T+3*D+6,c+R,c
 R=int(name[1]);shift={1:1,2:2,3:1}[R];base={1:2,2:4,3:7}[R]
 if name.endswith('a'):Y,C=Z;x=Y+shift;b0=base
 else:X,B,C=Z;x=X;b0=base+1+B
 c=C+2;return x,c+b0,c+R,c

@lru_cache(None)
def boundary_traces(name,Z):
 out=[]
 for L,row in zip(PERIODS,POLYS[name]):
  v=sum(coef*prod(z**p for z,p in zip(Z,e)) for e,coef in row[tuple(z%L for z in Z)])
  assert v.denominator==1
  out.append(v.numerator)
 return tuple(out)

@lru_cache(None)
def boundary_value(name,label,Z):
 v=sum(s*c*t for s,c,t in zip(SIZES,CHAR[LABELS.index(label)],boundary_traces(name,Z)))
 assert v%120==0
 return v//120

@lru_cache(None)
def boundary_constant(name,label,residue,order):
 ans=0
 for h in product(*(range(d+1) for d in order)):
  f=(-1)**(sum(order)-sum(h))*prod(comb(d,j) for d,j in zip(order,h))
  ans+=f*boundary_value(name,label,tuple(r+60*j for r,j in zip(residue,h)))
 assert ans>=0,(name,label,residue,order,ans)
 return ans

def boundary_tags(name,label,Z):
 residue=tuple(z%60 for z in Z);quotient=tuple(z//60 for z in Z)
 return [dict(branch=name,label=label,parameters=Z,residue=residue,quotient=quotient,order=o,constant=boundary_constant(name,label,residue,o)) for o in ORDERS[name]]

def boundary_coefficient(name,label,Z):
 return sum(t['constant']*prod(comb(q,j) for q,j in zip(t['quotient'],t['order'])) for t in boundary_tags(name,label,Z) if all(q>=j for q,j in zip(t['quotient'],t['order'])))

def constraints(tag):
 n=len(tag['parameters']);order=tag['order'];nv=n+1+sum(order)
 names=[f'q_{i}' for i in range(n)]+['selector']+[f'chain_{i}_{j+1}' for i,h in enumerate(order) for j in range(h)]
 eq=[];rhs=[];ge=[];grhs=[]
 for i in range(n):
  row=[0]*nv;row[i]=60;eq.append(row);rhs.append(tag['parameters'][i]-tag['residue'][i])
 start=n+1
 for axis,length in enumerate(order):
  for j in range(length-1):
   row=[0]*nv;row[start+j+1]=1;row[start+j]=-1;ge.append(row);grhs.append(1)
  if length:
   row=[0]*nv;row[axis]=1;row[start+length-1]=-1;ge.append(row);grhs.append(1)
  start+=length
 return dict(variables=names,integer=True,lower_bounds=[0]*nv,upper_bounds=list(tag['quotient'])+[tag['constant']-1]+[max(0,q-1) for q,j in zip(tag['quotient'],order) for _ in range(j)],A_eq=eq,b_eq=rhs,A_ge=ge,b_ge=grhs)

def witnesses(tag):
 if any(q<j for q,j in zip(tag['quotient'],tag['order'])):return
 for y in range(tag['constant']):
  for chains in product(*(combinations(range(q),j) for q,j in zip(tag['quotient'],tag['order']))):yield tuple(tag['quotient'])+(y,)+sum(chains,())

def route(x,b,k,c,d,mu):
 if any(type(v)is not int or v<0 for v in (x,b,k,c,d)):raise ValueError('parameters must be nonnegative integers')
 mu=tuple(mu)
 if mu not in LABELS:raise ValueError('outer must partition five')
 if not(c<k and b+c>=2*k and 2*b+x+3*c>=5*k):raise ValueError('require c<k,b+c>=2k,2b+x+3c>=5k')
 if c==0:return 'zero',(x,b,k,d,mu)
 if c==1:return 'one',(x,b,k,d,mu)
 R=k-c;b0=b-c;t=3*R-3-b0;gap=2*b0+x-5*R
 if t<0:
  if R>=4:return 'upper',(x,b,k,c,d,mu)
  shift={1:1,2:2,3:1}[R];base={1:2,2:4,3:7}[R]
  if b0==base:name=f'R{R}a';Z=(x-shift,c-2)
  else:name=f'R{R}b';Z=(x,b0-base-1,c-2)
 elif x<t:return 'lower',('B',(x,t-x-1,gap,c),d,mu)
 else:
  D=b0-2*R
  if D>=3:return 'lower',('A',(x-t,t,D-3,c),d,mu)
  name=f'D{D}';Z=(gap,t,c-2)
 assert name in RAW and min(Z)>=0,(name,Z,x,b,k,c)
 label=upper.transpose(mu) if (d+b+x+c)%2 else mu
 return name,(label,Z)
MODULES={'zero':zero,'one':one,'upper':upper,'lower':lower}

def coefficient(x,b,k,c,d=0,mu=(5,)):
 name,args=route(x,b,k,c,d,mu)
 if name in MODULES:return MODULES[name].coefficient(*args)
 return boundary_coefficient(name,*args)

def polytopes(x,b,k,c,d=0,mu=(5,)):
 name,args=route(x,b,k,c,d,mu)
 if name in MODULES:return dict(branch=name,parameters=args,formula=MODULES[name].polytopes(*args))
 return dict(branch=name,parameters=args,polytopes=[constraints(t) for t in boundary_tags(name,*args) if t['constant']])

def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('x','b','k','c'):p.add_argument('--'+name,type=int,required=True)
 p.add_argument('--d',type=int,default=0);p.add_argument('--outer',default='5');p.add_argument('--polytopes',action='store_true')
 v=p.parse_args();mu=tuple(map(int,v.outer.split(',')));r=dict(coefficient=coefficient(v.x,v.b,v.k,v.c,v.d,mu),route=route(v.x,v.b,v.k,v.c,v.d,mu))
 if v.polytopes:r['positive_formula']=polytopes(v.x,v.b,v.k,v.c,v.d,mu)
 print(json.dumps(r,indent=2))
if __name__=='__main__':main()
