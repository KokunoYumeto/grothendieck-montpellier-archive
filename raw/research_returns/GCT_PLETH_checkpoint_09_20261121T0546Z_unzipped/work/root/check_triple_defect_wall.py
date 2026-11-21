from pathlib import Path
from fractions import Fraction
from math import lcm,prod
from itertools import product
import json,sys
import numpy as np
sys.path.insert(0,'work/root')
from zero_twist_arrangement import traces as arrangement_traces
from five_row_cycle_trace import multiplicities,SIZES,CHARS,LABELS
DATA=json.loads(Path('work/root/TRIPLE_DEFECT_WALL_CHECK.json').read_text())
PERIODS=(1,2,2,3,6,4,5)
POLYS=[{tuple(map(int( ),key.split(','))): [] for key in []}] if False else []
for row in DATA['phase_polynomials']:
 POLYS.append({tuple(map(int,key.split(','))):[(tuple(map(int,power.split(','))),Fraction(*value)) for power,value in poly.items()] for key,poly in row.items()})
def values(params):
 out=[]
 for L,cls in zip(PERIODS,POLYS):
  poly=cls[tuple(x%L for x in params)]
  v=sum(c*prod(x**p for x,p in zip(params,e)) for e,c in poly)
  assert v.denominator==1
  out.append(v.numerator)
 return tuple(out)
checks=0;actual=0
for t,K,X in product(range(3),range(2),range(4)):
 k=t+6+K;x=t+X;b=3*k-3-t
 got=values((X,t,K));expected=arrangement_traces(x,b,k)
 assert got==expected,(t,K,X,got,expected)
 checks+=7
 if X<2:
  f=tuple(sum(s*c*v for s,c,v in zip(SIZES,row,got))//120 for row in CHARS)
  if (b+x)%2:f=f[::-1]
  lam=(3*b+2*x-5*k,b+x,b+x,x,0)
  expected=multiplicities(lam)
  assert f==expected,(lam,f,expected)
  actual+=7
print('direct checks',checks,'actual',actual,flush=True)
traces=[];boundmax=0
for L,cls in zip(PERIODS,POLYS):
 arr=np.empty((60,60,60),dtype=np.int64)
 for phase,poly in cls.items():
  D=lcm(*(v.denominator for e,v in poly)) if poly else 1
  bound=sum(abs(int(c*D))*59**sum(e) for e,c in poly)
  assert bound<2**63;boundmax=max(boundmax,bound)
  coords=[np.arange(r,60,L,dtype=np.int64) for r in phase]
  X=coords[0][:,None,None];T=coords[1][None,:,None];K=coords[2][None,None,:]
  value=np.zeros((len(coords[0]),len(coords[1]),len(coords[2])),dtype=np.int64)
  for e,c in poly:
   value+=int(c*D)*X**e[0]*T**e[1]*K**e[2]
  assert np.all(value%D==0)
  arr[phase[0]::L,phase[1]::L,phase[2]::L]=value//D
 traces.append(arr)
constants=[];zeros={};hashes={}
import hashlib
for label,row in zip(LABELS,CHARS):
 bound=sum(abs(s*c)*int(np.max(np.abs(v))) for s,c,v in zip(SIZES,row,traces));assert bound<2**63
 numerator=sum(s*c*v for s,c,v in zip(SIZES,row,traces))
 assert np.all(numerator%120==0)
 val=numerator//120
 assert int(val.min())>=0,(label,int(val.min()))
 zeros[label]=np.argwhere(val==0).tolist()
 hashes[label]={'min':int(val.min()),'max':int(val.max()),'sha256':hashlib.sha256(np.ascontiguousarray(val,dtype='<i8').tobytes()).hexdigest()}
 constants.append(val)
print('base constants PASS',1512000,'zeros',zeros,flush=True)
receipt={'statement':'G-033-candidate','direct_restriction_trace_checks':checks,'actual_balanced_coefficient_checks':actual,'base_constants':1512000,'zero_parameters':zeros,'label_arrays':hashes,'polynomial_integer_operation_bound':boundmax,'outcome':'PASS'}
Path('work/root/TRIPLE_DEFECT_WALL_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
