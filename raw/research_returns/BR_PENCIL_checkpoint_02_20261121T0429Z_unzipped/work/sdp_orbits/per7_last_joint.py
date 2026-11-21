"""Joint A/B refinement of the final permanent support11 seven-plane."""
from pathlib import Path
import sys,json,time
from itertools import combinations
import numpy as np
from sympy import Matrix
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
from det7_prolongation import data,prolong,var_weight,quad_weight
from check_support9_sevenplanes import arrangements,integer_rows,primitive,rank_q

S=[0,1,2,6,7,18,19]

def setup():
 variables,T,blocks,image=data(S,1);U=[T[:,:,c] for c in range(len(variables))]
 fixed=23;w,coords,d=blocks[fixed];params=coords[:-1] if w in image else coords;assert d==1
 q,v=params[0];X=np.zeros(T.shape[:2],dtype=np.int64);X[q,v]=1;U0=U+[X]
 return variables,T,blocks,image,U,U0,(q,v)


def conditions_for(variables,T,blocks,image,U0,coordinate,index,orientation):
 w,coords,d=blocks[index];params=coords[:-1] if w in image else coords
 X=[]
 for q,v in params:
  M=np.zeros(T.shape[:2],dtype=np.int64);M[q,v]=1;X.append(M)
 M0=prolong(U0,orientation);MX=prolong(X,orientation)
 aw=[tuple(-x for x in quad_weight(q)) for q in S];bw=[var_weight(v) for v in variables]
 ow,fw=(aw,bw) if orientation=='B' else (bw,aw)
 pairs=list(combinations(range(len(fw)),2))
 rw=[tuple(x+y+z for x,y,z in zip(q,fw[i],fw[j])) for q in ow for i,j in pairs]
 ub=[tuple(-x for x in v) for v in bw];q,v=coordinate;ub.append(tuple(x+y for x,y in zip(aw[q],bw[v])))
 cw=[tuple(x+y for x,y in zip(v,u)) for u in ub for v in fw]
 output=[]
 for j,weight in enumerate(fw):
  target=tuple(x+y for x,y in zip(w,weight));rows=[i for i,x in enumerate(rw) if x==target];cols=[i for i,x in enumerate(cw) if x==target]
  B=Matrix(M0[np.ix_(rows,cols)].tolist()) if cols else Matrix.zeros(len(rows),0)
  N=B.T.nullspace();H=Matrix([primitive(v) for v in N]) if N else Matrix.zeros(0,len(rows))
  Q=Matrix(MX[np.ix_(rows,[s*len(fw)+j for s in range(d)])].tolist()) if rows else Matrix.zeros(0,d)
  out=H*Q;output.append({'equations':integer_rows(out),'target':target})
 return output


def main():
 variables,T,blocks,image,U,U0,coordinate=setup();out=[]
 print('variables',variables,'fixed',coordinate,flush=True)
 for index in [1,5,19,20,21,22,24,25]:
  A=conditions_for(variables,T,blocks,image,U0,coordinate,index,'A');B=conditions_for(variables,T,blocks,image,U0,coordinate,index,'B')
  cond=[x['equations'] for x in A+B];d=blocks[index][2];states=arrangements(cond,d);surv=[]
  for st in states:
   zeros=st['zero_columns'];incA=7-sum(z<7 for z in zeros);incB=11-sum(z>=7 for z in zeros)
   if incA<=6 and incB<=7:surv.append({'parameter_basis':st['basis'],'dimension':st['dimension'],'increment_A':incA,'increment_B':incB,'zero_columns':sorted(zeros)})
  params=blocks[index][1][:-1] if blocks[index][0] in image else blocks[index][1]
  rec={'index':index,'weight':blocks[index][0],'parameter_coordinates':params,'quotient_dimension':d,'arrangement_states':len(states),'survivors':surv};out.append(rec)
  print(rec,flush=True)
 Path(__file__).with_name('per7_last_joint.json').write_text(json.dumps({'subset':S,'fixed_coordinate':coordinate,'records':out},indent=2)+'\n')

if __name__=='__main__':main()
