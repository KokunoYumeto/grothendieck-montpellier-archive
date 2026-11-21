"""G038: stable tails (a,2), by free modules and a weighted Koszul cycle."""
from functools import lru_cache
from collections import Counter
import argparse,json
import stable_hook_positive as H

def corners(lam):
 out=[]
 for i,v in enumerate(lam):
  if i+1<len(lam) and lam[i+1]==v:continue
  q=list(lam);q[i]-=1
  while q and not q[-1]:q.pop()
  out.append(tuple(q))
 return out
def add_box(lam):
 out=[]
 for i in range(len(lam)+1):
  if i and i<len(lam) and lam[i-1]==lam[i]:continue
  if i==len(lam):q=lam+(1,)
  else:q=lam[:i]+(lam[i]+1,)+lam[i+1:]
  out.append(q)
 return out
def strip(big,small,horizontal):
 b=big+(0,);s=small+(0,)*(len(b)-len(small))
 if any(s[i]>b[i] for i in range(len(b))):return False
 if horizontal:return all(b[i]>=s[i]>=b[i+1] for i in range(len(b)-1))
 return all(b[i]-s[i]<=1 for i in range(len(b)))
def tensor_standard(nu):
 out=Counter()
 for beta in corners(nu):
  for alpha in add_box(beta):out[alpha]+=1
 out[nu]-=1
 assert all(v>=0 for v in out.values())
 return {k:v for k,v in out.items() if v}
def tensor_symmetric_square(nu):
 out=Counter()
 lowers={b for x in corners(nu) for b in corners(x)}
 for beta in lowers:
  uppers={a for x in add_box(beta) for a in add_box(x)}
  for horizontal in (False,True):
   if strip(nu,beta,horizontal):
    for alpha in uppers:
     if strip(alpha,beta,horizontal):out[alpha]+=1
 return dict(out)
def weighted_fake(mult,m):
 out=[0]*(m*(m-1)//2+1)
 for nu,c in mult.items():
  for i,v in enumerate(H.fake_degree(nu)):out[i]+=c*v
 return H.trim(out)
def shifted_sum(terms):
 N=max((k+len(p) for p,k,c in terms),default=1)
 out=[0]*N
 for p,k,c in terms:
  for i,v in enumerate(p):out[i+k]+=c*v
 return H.trim(out)
@lru_cache(None)
def free_numerator(nu):
 nu=tuple(nu);m=sum(nu)
 if m<3 or not H.valid_partition(nu,m):raise ValueError('require a partition of m>=3')
 d=1 if nu==(m-1,1) else 2 if nu==(m-2,1,1) else 0
 terms=[(weighted_fake(tensor_symmetric_square(nu),m),2,1),
        (weighted_fake(tensor_standard(nu),m),1,-1)]
 if d:terms.append(([1,0]+[-1]*(m-1),d,1))
 F=shifted_sum(terms)
 assert all(v>=0 for v in F),(nu,F)
 assert len(F)<=m*(m-1)//2+3
 return tuple(F),d
def module_coefficient(m,a,nu):
 nu=tuple(nu)
 if m<3 or a<2 or not H.valid_partition(nu,m):raise ValueError('invalid second-row module')
 F,d=free_numerator(nu);D=a+2
 value=H.rational_coefficient(F,H.denominator(2,m),D)
 if d:value+=H.module_coefficient(m,D-d-1,1,(m,))
 return value
def module_support(m,a,nu):
 F,d=free_numerator(tuple(nu));D=a+2
 free=any(c and D-j>=0 and D-j!=1 for j,c in enumerate(F))
 cycles=bool(d and H.module_support(m,D-d-1,1,(m,)))
 return free or cycles
def physical(m,a,t,n,mu):
 mu=tuple(mu)
 if any(type(x)is not int for x in (m,a,t,n)) or m<3 or a<2 or t<0 or n<a+t or not H.valid_partition(mu,m):raise ValueError('invalid stable second-row parameters')
 lam=(m*n-a-2-(m-1)*t,a+t,t+2)+(t,)*(m-3)
 assert lam[0]>=lam[1]>=lam[2] and sum(lam)==m*n
 return lam,H.transpose(mu) if t%2 else mu
def coefficient(m,a,t,n,mu):
 _,nu=physical(m,a,t,n,mu)
 return module_coefficient(m,a,nu)
def module_polytopes(m,a,nu):
 nu=tuple(nu);F,d=free_numerator(nu);D=a+2;out=[]
 for j,c in enumerate(F):
  if c<=0 or D<j:continue
  P=H.Matrix();label=P.var('generator',0,c-1)
  coins={i:P.var(f'c{i}',0,(D-j)//i) for i in range(2,m+1)}
  P.row({coins[i]:i for i in coins},'=',D-j)
  out.append({'tag':{'kind':'free','degree':j,'multiplicity':c},**P.data()})
 if d:out.append({'tag':{'kind':'weighted_koszul','shift':d},**H.module_polytope(m,D-d-1,1,(m,))})
 return out
def polytopes(m,a,t,n,mu):
 lam,nu=physical(m,a,t,n,mu)
 return {'partition':lam,'outer':tuple(mu),'effective_outer':nu,'polytopes':module_polytopes(m,a,nu)}
def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('m','a','t','n'):p.add_argument('--'+name,type=int,required=True)
 p.add_argument('--outer',required=True);p.add_argument('--polytopes',action='store_true');v=p.parse_args()
 mu=tuple(map(int,v.outer.split(',')));args=(v.m,v.a,v.t,v.n,mu)
 result={'statement':'G-038','coefficient':coefficient(*args),'partition':physical(*args)[0]}
 if v.polytopes:result.update(polytopes(*args))
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
