#!/usr/bin/env python3
"""Explore the joint (110),(101),(011),(111) border-apolarity conditions.
This is an exact finite-flag probe. Continuous branches are explicitly OPEN.
"""
import argparse,json,time
from collections import defaultdict,Counter
from itertools import combinations_with_replacement
from br_linear import Space,rank,rowspace,nullspace,wedge,add
from borel_quiver import ab_module,module,successors,extension_vectors,variable_roots,linear_combination


def wedge_ranks(E,a,b):
 return {o:rank([wedge(v,o,i) for v in E for i in range(a if o=='A' else b)]) for o in ('A','B')}


def enumerate_ab(M,r):
 a=len(M['subset']);b=len(M['support']);states={tuple(() for _ in M['blocks'])};families=[];history=[]
 for level in range(1,r-b+1):
  nxt=set()
  for F in states:
   rigid,param=successors(M,F);nxt.update(rigid)
   for i,K in param:families.append((level,F,i,K))
  states=set();excluded=0
  for F in nxt:
   E=M['U']+extension_vectors(M,F);rs=wedge_ranks(E,a,b)
   if any(rs[o]>(d-1)*r for o,d in (('A',a),('B',b))):excluded+=1
   else:states.add(F)
  history.append([level,len(nxt),excluded,len(states),len(families)])
  print('AB',M['subset'],history[-1],flush=True)
 return [M['U']+extension_vectors(M,F) for F in states],families,history


def intersection(E,F,a,b):
 # V=(C tensor E_AB) intersect (B tensor F_AC).
 other=Space()
 for v in F:other.append(v)
 left=[];eqcols=[]
 for v in E:
  for c in range(b):
   w={(h,z,c):x for (h,z),x in v.items()};left.append(w);parts=defaultdict(dict)
   for (h,z,c),x in w.items():parts[z][h,c]=x
   out={}
   for z,part in parts.items():
    for hc,x in other.reduce(part).items():out[z,hc]=x
   eqcols.append(out)
 rows=defaultdict(dict)
 for j,col in enumerate(eqcols):
  for i,x in col.items():rows[i][j]=x
 K=nullspace([tuple(v.items()) for v in rows.values()],len(eqcols))
 return [linear_combination(left,v) for v in K]


def bc_support(V,a):
 result=[]
 for v in V:
  parts=defaultdict(dict)
  for (h,b,c),x in v.items():parts[h][b,c]=x
  result.extend(parts.values())
 return result


def construct_bc(M,V):
 a=len(M['subset']);b=len(M['support']);U=[{} for _ in range(a)]
 for c,vec in enumerate(M['U']):
  for (h,z),x in vec.items():U[h][z,c]=x
 roots=[]
 for vr in variable_roots(M['support']):
  def action(i,vr=vr):
   b,c=i;out={(z,c):x for z,x in vr(b).items()}
   for z,x in vr(c).items():out[b,z]=out.get((b,z),0)+x
   return out
  roots.append(action)
 weight=lambda x:add(M['bw'][x[0]],M['bw'][x[1]])
 out=module(U,bc_support(V,a),weight,roots);out['V']=V
 return out


def joint_kernel(V,E):
 s=Space()
 for v in E:s.append(v)
 cols=[]
 for v in V:
  parts=defaultdict(dict)
  for (a,b,c),x in v.items():parts[a][b,c]=x
  col={}
  for a,vec in parts.items():
   for bc,x in s.reduce(vec).items():col[a,bc]=x
  cols.append(col)
 return len(V)-rank(cols)


def enumerate_bc(M,a,b,r):
 states={tuple(() for _ in M['blocks'])};families=[];history=[]
 for level in range(1,r-a+1):
  nxt=set()
  for F in states:
   rigid,param=successors(M,F);nxt.update(rigid)
   for i,K in param:families.append((level,F,i,K))
  states=set();excluded=0;lastdim=[]
  for F in nxt:
   E=M['U']+extension_vectors(M,F);rs=wedge_ranks(E,b,b)
   if any(rs[o]>(b-1)*r for o in ('A','B')):excluded+=1;continue
   if level==r-a:
    d=joint_kernel(M['V'],E);lastdim.append(d)
    if d<r:excluded+=1;continue
   states.add(F)
  history.append([level,len(nxt),excluded,len(states),len(families)])
  print('BC',history[-1],flush=True)
 return {'history':history,'parameter_branches':len(families),'survivors':len(states),'final_kernel_dimensions':lastdim,
         'status':'EXCLUDED' if not families and not states else 'OPEN'}


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--subset',type=int,nargs='+',default=[0,1,2,3,4,5,6,7,8,12]);ap.add_argument('--pair',type=int,nargs=2);ap.add_argument('--output');args=ap.parse_args()
 start=time.time();S=args.subset;M=ab_module(S);a=len(S);b=len(M['support'])
 Es,fams,hist=enumerate_ab(M,17);print('AB final',len(Es),'families',len(fams),flush=True)
 results=[]
 pairs=[tuple(args.pair)] if args.pair else list(combinations_with_replacement(range(len(Es)),2))
 for i,j in pairs:
  V=intersection(Es[i],Es[j],a,b);B=construct_bc(M,V)
  print('PAIR',i,j,'Vdim',len(V),'quotientRdim',sum(len(v) for w,v in B['blocks']),flush=True)
  result=enumerate_bc(B,a,b,17);result.update({'pair':[i,j],'V_dimension':len(V),'quotientR_dimension':sum(len(v) for w,v in B['blocks'])});results.append(result)
 out={'subset':S,'AB_history':hist,'AB_families':len(fams),'AB_candidates':len(Es),'results':results,'seconds':time.time()-start}
 if args.output:open(args.output,'w').write(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out),flush=True)
if __name__=='__main__':main()
