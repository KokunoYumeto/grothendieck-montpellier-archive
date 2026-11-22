#!/usr/bin/env python3
"""Independent first-stage enumeration and P_(2,2) test, stdlib only.
Supports characteristic zero and any input prime; tensor symmetry means the
invariant subspace of the tensor square, also in characteristic two.
"""
import argparse,json,time
from collections import defaultdict
from br_linear import setup,rank,rowspace,nullspace,wedge,Space
from check_twodim_extensions import run


def arrangements(conditions,d,p):
 spaces={()}
 for C in conditions:
  spaces.update(F for E in tuple(spaces) if len(F:=rowspace(E+C,p))<d)
 out=[]
 for E in sorted(spaces):
  zeros={j for j,C in enumerate(conditions) if rowspace(E+C,p)==E}
  out.append((E,zeros))
 return out


def prolongation22(U,a,b,p):
 # First kernel, E tensor B -> A tensor exterior^2 B.
 columns=[wedge(v,'B',j) for v in U for j in range(b)]
 rows=defaultdict(dict)
 for j,v in enumerate(columns):
  for k,x in v.items():rows[k][j]=x
 K=nullspace([tuple(v.items()) for v in rows.values()],len(columns),p)
 base_rank=len(columns)-len(K)
 symmetric=[]
 for v in K:
  z=defaultdict(int)
  for c,x in v.items():
   e,j=divmod(c,b)
   for (i,h),y in U[e].items():z[i,h,j]+=x*y
  if p:z={i:x%p for i,x in z.items()}
  assert all(x==z.get((i,k,j),0) for (i,j,k),x in z.items())
  symmetric.append({(i,j,k):x for (i,j,k),x in z.items() if j<=k and x})
 second=[]
 for v in symmetric:
  for h in range(a):
   z={}
   for (i,j,k),x in v.items():
    if i==h:continue
    key=(min(i,h),max(i,h),j,k)
    z[key]=z.get(key,0)+(x if i<h else -x)
   second.append(z)
 r22=rank(second,p)
 return {'first_rank':base_rank,'first_kernel_dim':len(K),
         'second_rank':r22,'second_domain_dim':len(second),
         'P22_dimension':len(second)-r22}


def check(S,sign,p):
 start=time.time();initial=run('higher_stage',sign,S,p)
 D=setup(S,sign,p);m=len(D['support']);a=len(S);dims=[len(c) for w,c in D['blocks']]
 fixed=[];details=[]
 for pair in initial['survivors']:
  assert len(pair)==2
  i,j=pair
  if dims[i]!=1:i,j=j,i
  assert dims[i]==1
  extra=D['blocks'][i][1]
  C=setup(S,sign,p,extra);raw=C['maps']['A'][j]+C['maps']['B'][j]
  states=arrangements([cond for w,cols,cond in raw],dims[j],p)
  good=[]
  for E,zeros in states:
   if C['base_ranks']['A']+a-len(zeros&set(range(a)))>(a-1)*13:continue
   if C['base_ranks']['B']+m-len(zeros&set(range(a,a+m)))>(m-1)*13:continue
   K=nullspace(E,dims[j],p)
   assert len(K)==1,'a positive-dimensional extension family survives'
   v={D['blocks'][j][1][t]:x for t,x in K[0].items()}
   P=prolongation22(C['U']+[v],a,m,p)
   assert P['P22_dimension']<13
   good.append({'parameter_vector':[[t,str(x)] for t,x in sorted(K[0].items())],**P})
  details.append({'pair':pair,'fixed_block':i,'variable_block':j,'arrangement_states':len(states),'remaining_lines':good})
 out={'subset':S,'sign':sign,'prime':p,'initial_choices':initial['quotient_choices'],
      'initial_surviving_pairs':initial['survivors'],'final_extensions':details,'status':'PASS','seconds':time.time()-start}
 print(json.dumps(out),flush=True);return out


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,default=0)
 ap.add_argument('--case',choices=['P19','P09_A'],default='P19');ap.add_argument('--output');args=ap.parse_args()
 if args.prime:assert args.prime>=2 and all(args.prime%d for d in range(2,int(args.prime**.5)+1))
 S=[0,1,2,6,7,18,19] if args.case=='P19' else [0,1,3,6,7,9,12]
 result=check(S,1 if args.case=='P19' else -1,args.prime)
 if args.output:
  with open(args.output,'w') as f:json.dump(result,f,indent=2);f.write('\n')
if __name__=='__main__':main()
