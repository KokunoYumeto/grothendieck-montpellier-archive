"""Exploratory higher bidegree prolongations of the eight fixed AB candidates."""
from pathlib import Path
import json,time,sys
from itertools import combinations_with_replacement
import numpy as np
from sympy import Matrix
from per7_last_joint import setup,S
from per7_last_111 import extension
from det7_prolongation import prolong,rank
from det7_typeB_line_conditions import primitive


def symmetric_prolongation(basis,orientation):
 M=Matrix(prolong(basis,orientation).tolist());K=M.nullspace();nA,nB=basis[0].shape
 factor=nB if orientation=='B' else nA
 pairs=list(combinations_with_replacement(range(factor),2));out=[]
 for k in K:
  coeff=primitive(k);T=np.zeros((nA,nB,factor),dtype=np.int64)
  for s,E in enumerate(basis):
   for j in range(factor):T[:,:,j]+=coeff[s*factor+j]*E
  if orientation=='B':
   assert np.array_equal(T,T.transpose(0,2,1))
   N=np.stack([T[:,i,j] for i,j in pairs],axis=1)
  else:
   assert np.array_equal(T,T.transpose(2,1,0))
   N=np.stack([T[i,:,j] for i,j in pairs],axis=0)
  out.append(N)
 return out


def main():
 variables,T,blocks,image,U,U0,coordinate=setup();out=[]
 for v in [1,2,3,5,6,7,9,10]:
  E=extension(v,U0);F12=symmetric_prolongation(E,'B');F21=symmetric_prolongation(E,'A');assert len(F12)==len(F21)==13
  M22=prolong(F12,'A');r22=rank(M22)[0];dim22=M22.shape[1]-r22
  # Multiplication in the already symmetric B index needs a higher-order
  # symmetry operator; this first test is the exact mixed bidegree22.
  rec={'v':v,'F12_dim':len(F12),'F21_dim':len(F21),'F22_matrix_shape':list(M22.shape),'F22_nullity_upper':dim22,'rank_mod1000003':r22};out.append(rec);print(rec,flush=True)
 Path(__file__).with_name('per7_last_higher_prolongation.json').write_text(json.dumps({'subset':S,'records':out},indent=2)+'\n')

if __name__=='__main__':
 st=time.time();main();print('seconds',time.time()-st)
