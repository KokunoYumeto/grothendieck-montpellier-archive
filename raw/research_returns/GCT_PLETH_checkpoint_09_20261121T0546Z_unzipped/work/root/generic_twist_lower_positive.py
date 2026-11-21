"""G035 positive formulas on the two arbitrary-twist lower cones."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb,prod
import sys,json,argparse
HERE=Path(__file__).resolve().parent
sys.path.append(str(HERE.parent/'theta'/'outer5'/'variable_wall'))
from generic_twist_upper_positive import LABELS,CHAR,SIZES,transpose,constraints,witnesses
PERIODS=(1,2,2,3,6,4,5)
RAW={branch:json.loads((HERE/f'GENERIC_TWIST_LOWER_{branch}_CHECK.json').read_text()) for branch in ('A','B')}
POLYS={branch:[{tuple(map(int,key.split(','))):tuple((tuple(map(int,e.split(','))),Fraction(*v)) for e,v in p.items()) for key,p in row.items()} for row in d['phase_polynomials']] for branch,d in RAW.items()}
ORDERS={branch:((0,0,0,0),)+tuple(map(tuple,d['active_orders'])) for branch,d in RAW.items()}

def physical(branch,Z):
 X,T,K,C=Z
 if branch=='A':return X+T,C+2*T+15+3*K,C+T+6+K,C
 if branch=='B':return X,C+2*X+5*T+20+3*K,C+X+2*T+8+K,C
 raise ValueError('branch must be A or B')

@lru_cache(None)
def traces(branch,Z):
 answer=[]
 for L,row in zip(PERIODS,POLYS[branch]):
  value=sum(v*prod(z**p for z,p in zip(Z,e)) for e,v in row[tuple(z%L for z in Z)])
  assert value.denominator==1
  answer.append(value.numerator)
 return tuple(answer)

@lru_cache(None)
def fixed_value(branch,label,Z):
 total=sum(s*c*t for s,c,t in zip(SIZES,CHAR[LABELS.index(label)],traces(branch,Z)))
 assert total%120==0
 return total//120

@lru_cache(None)
def constant(branch,label,residue,order):
 total=0
 for h in product(*(range(d+1) for d in order)):
  f=(-1)**(sum(order)-sum(h))*prod(comb(d,j) for d,j in zip(order,h))
  total+=f*fixed_value(branch,label,tuple(r+60*j for r,j in zip(residue,h)))
 assert total>=0,(branch,label,residue,order,total)
 return total

def parameters(branch,Z,d,mu):
 Z=tuple(Z);mu=tuple(mu)
 if branch not in RAW or len(Z)!=4:raise ValueError('branch A/B and four coordinates required')
 if any(type(v)is not int or v<0 for v in Z+(d,)):raise ValueError('coordinates and d must be nonnegative integers')
 if mu not in LABELS:raise ValueError('outer must partition five')
 x,b,k,c=physical(branch,Z)
 label=transpose(mu) if (d+b+x+c)%2 else mu
 return label,tuple(z%60 for z in Z),tuple(z//60 for z in Z)

def coefficient(branch,Z,d=0,mu=(5,)):
 Z=tuple(Z);label,residue,quotient=parameters(branch,Z,d,mu)
 return sum(constant(branch,label,residue,o)*prod(comb(q,j) for q,j in zip(quotient,o)) for o in ORDERS[branch] if all(q>=j for q,j in zip(quotient,o)))

def tags(branch,Z,d=0,mu=(5,)):
 Z=tuple(Z);label,residue,quotient=parameters(branch,Z,d,mu)
 return [dict(branch=branch,label=label,parameters=Z,residue=residue,quotient=quotient,order=o,constant=constant(branch,label,residue,o)) for o in ORDERS[branch]]

def polytopes(branch,Z,d=0,mu=(5,)):
 return [constraints(t) for t in tags(branch,Z,d,mu) if t['constant']]

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--branch',choices=('A','B'),required=True)
 p.add_argument('--coordinates',type=int,nargs=4,required=True);p.add_argument('--d',type=int,default=0);p.add_argument('--outer',default='5');p.add_argument('--polytopes',action='store_true')
 v=p.parse_args();mu=tuple(map(int,v.outer.split(',')));x,b,k,c=physical(v.branch,v.coordinates)
 r={'branch':v.branch,'coordinates':v.coordinates,'physical':{'x':x,'b':b,'k':k,'c':c},'inner':v.d+b+x+c-k,'output':[v.d+3*b+2*x+4*c-5*k,v.d+b+x+c,v.d+b+x,v.d+x,v.d],'coefficient':coefficient(v.branch,v.coordinates,v.d,mu)}
 if v.polytopes:r['polytopes']=polytopes(v.branch,v.coordinates,v.d,mu)
 print(json.dumps(r,indent=2))
if __name__=='__main__':main()
