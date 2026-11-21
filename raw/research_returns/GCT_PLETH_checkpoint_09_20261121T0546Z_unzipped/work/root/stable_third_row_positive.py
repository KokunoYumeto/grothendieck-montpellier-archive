"""G039: checked positive construction for stable (a,3) tails."""
from functools import lru_cache
from collections import Counter
import argparse,json
import stable_hook_positive as H
import stable_second_row_positive as S

def linear_combination(terms):
 out=Counter()
 for c,data in terms:
  for nu,v in data.items():out[nu]+=c*v
 return {nu:v for nu,v in out.items() if v}
@lru_cache(None)
def W(nu):return S.tensor_standard(nu)
@lru_cache(None)
def S2(nu):return S.tensor_symmetric_square(nu)
def compose(data,operator):
 out=Counter()
 for nu,c in data.items():
  for alpha,v in operator(nu).items():out[alpha]+=c*v
 return dict(out)
def remove_paths(nu,k):
 data={nu:1}
 for _ in range(k):
  out=Counter()
  for lam,v in data.items():
   for beta in S.corners(lam):out[beta]+=v
  data=out
 return data
def add_paths(nu,k):
 data={nu:1}
 for _ in range(k):
  out=Counter()
  for lam,v in data.items():
   for alpha in S.add_box(lam):out[alpha]+=v
  data=out
 return data
def lr3(big,small):
 hor=int(S.strip(big,small,True));vert=int(S.strip(big,small,False))
 mixed=sum(S.strip(gamma,small,True) for gamma in S.corners(big))-hor
 assert mixed>=0
 return (hor,mixed,vert)
@lru_cache(None)
def S3(nu):
 ordered=Counter()
 for beta,c in remove_paths(nu,2).items():
  for alpha,v in add_paths(beta,2).items():ordered[alpha]+=c*v
 triples=Counter()
 for beta in remove_paths(nu,3):
  left=lr3(nu,beta)
  for alpha in add_paths(beta,3):
   right=lr3(alpha,beta)
   triples[alpha]+=sum(x*y for x,y in zip(left,right))
 out=linear_combination([(1,ordered),(1,triples),(-1,S2(nu))])
 assert all(v>=0 for v in out.values())
 return out
@lru_cache(None)
def S21(nu):
 out=linear_combination([(1,compose(S2(nu),W)),(-1,S3(nu))])
 assert all(v>=0 for v in out.values())
 return out
@lru_cache(None)
def S22(nu):
 out=linear_combination([(1,compose(S2(nu),S2)),(-1,compose(S3(nu),W))])
 assert all(v>=0 for v in out.values())
 return out
@lru_cache(None)
def free_numerator(nu):
 m=sum(nu)
 if m<4 or not H.valid_partition(nu,m):raise ValueError('require a partition of m>=4')
 trivial=(m,)
 c2=S2(nu).get(trivial,0);c21=S21(nu).get(trivial,0)
 cw=S22(nu).get(trivial,0)-c2
 assert min(c2,c21,cw)>=0
 terms=[(S.weighted_fake(S3(nu),m),3,1),(S.weighted_fake(S2(nu),m),2,-1)]
 weights=(4,)+tuple(range(3,m+1))
 for shift,mult,rel in ((2,c2,weights),(3,c21,tuple(range(2,m+1))),(4,cw,tuple(range(2,m+1)))):
  if mult:
   terms.append(([mult],shift,1))
   for degree in rel:terms.append(([mult],shift+degree,-1))
 out=S.shifted_sum(terms)
 assert all(v>=0 for v in out),(nu,out,c2,c21,cw)
 return tuple(out),(c2,c21,cw)
def cycle_coefficient(weights,D):
 if D<0:return 0
 total=0
 for i,wi in enumerate(weights):
  q=[1]
  for w in weights[i:]:q=H.mul(q,[1]+[0]*(w-1)+[-1])
  p=[0]*(wi+max(weights,default=0)+1)
  for wj in weights[i+1:]:p[wi+wj]+=1
  total+=H.rational_coefficient(H.trim(p),q,D)
 return total
def module_coefficient(m,a,nu):
 nu=tuple(nu)
 if m<3 or a<3 or not H.valid_partition(nu,m):raise ValueError('invalid third-row module')
 if m==3:
  eff=H.transpose(nu)
  return int(eff==(3,)) if a==3 else H.module_coefficient(3,a-3,0,eff)
 F,(c2,c21,cw)=free_numerator(nu);D=a+3
 ans=H.rational_coefficient(F,H.denominator(2,m),D)
 ordinary=tuple(range(2,m+1));modified=(4,)+tuple(range(3,m+1))
 if c21:ans+=c21*cycle_coefficient(ordinary,D-3)
 if cw:ans+=cw*cycle_coefficient(ordinary,D-4)
 if c2:ans+=c2*(cycle_coefficient(modified,D-2)+cycle_coefficient(modified,D-4))
 return ans
def module_support(m,a,nu):
 nu=tuple(nu)
 if m==3:
  return any(c and a-3-j>=0 and a-3-j!=1 for j,c in enumerate(H.fake_degree(H.transpose(nu))))
 F,(c2,c21,cw)=free_numerator(nu);D=a+3
 return (any(c and D-j>=0 and D-j!=1 for j,c in enumerate(F))
         or bool(c21 and D>=8) or bool((c2 or cw) and D>=9))
def physical(m,a,t,n,mu):
 mu=tuple(mu)
 if any(type(x)is not int for x in (m,a,t,n)) or m<3 or a<3 or t<0 or n<a+t or not H.valid_partition(mu,m):raise ValueError('invalid stable third-row parameters')
 lam=(m*n-a-3-(m-1)*t,a+t,t+3)+(t,)*(m-3)
 assert lam[0]>=lam[1]>=lam[2] and sum(lam)==m*n
 return lam,H.transpose(mu) if t%2 else mu
def coefficient(m,a,t,n,mu):
 _,nu=physical(m,a,t,n,mu)
 return module_coefficient(m,a,nu)
def cycle_polytope(weights,D,multiplicity,extra_bit=False):
 P=H.Matrix();k=len(weights)
 g=P.var('generator',0,multiplicity-1)
 z={j:P.var(f'z{j}',0,1) for j in range(k)}
 y={j:P.var(f'y{j}',0,1) for j in range(k)}
 b={j:P.var(f'b{j}',0,max(0,D)//weights[j]) for j in range(k)}
 P.row({v:1 for v in z.values()},'=',1);P.row({v:1 for v in y.values()},'=',1)
 for j in range(k):
  P.row({y[j]:1,**{z[i]:-1 for i in range(j)}},'<=',0)
  P.row({b[j]:1,z[j]:-1,y[j]:-1},'>=',0)
  P.row({b[j]:1,**{z[i]:-max(0,D) for i in range(j+1)}},'<=',0)
 degree={b[j]:weights[j] for j in range(k)}
 if extra_bit:degree[P.var('quadratic_remainder',0,1)]=2
 P.row(degree,'=',D)
 return P.data()
def module_polytopes(m,a,nu):
 nu=tuple(nu)
 if m==3:
  eff=H.transpose(nu)
  out=[]
  for j,c in enumerate(H.fake_degree(eff)):
   if not c or j>a-3:continue
   P=H.Matrix();P.var('generator',0,c-1)
   b={i:P.var(f'c{i}',0,(a-3-j)//i) for i in (2,3)}
   P.row({b[i]:i for i in b},'=',a-3-j)
   out.append({'tag':{'kind':'free_rank_two','degree':j,'multiplicity':c},**P.data()})
  return out
 F,(c2,c21,cw)=free_numerator(nu);D=a+3;out=[]
 for j,c in enumerate(F):
  if not c or j>D:continue
  P=H.Matrix();P.var('generator',0,c-1)
  b={i:P.var(f'c{i}',0,(D-j)//i) for i in range(2,m+1)}
  P.row({b[i]:i for i in b},'=',D-j)
  out.append({'tag':{'kind':'free','degree':j,'multiplicity':c},**P.data()})
 for kind,shift,mult,weights,bit in [('ordinary',3,c21,tuple(range(2,m+1)),False),('ordinary',4,cw,tuple(range(2,m+1)),False),('quadratic',2,c2,(4,)+tuple(range(3,m+1)),True)]:
  if mult:out.append({'tag':{'kind':kind,'shift':shift,'multiplicity':mult,'weights':weights,'extra_bit':bit},**cycle_polytope(weights,D-shift,mult,bit)})
 return out
def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('m','a','t','n'):p.add_argument('--'+name,type=int,required=True)
 p.add_argument('--outer',required=True);p.add_argument('--polytopes',action='store_true');v=p.parse_args()
 mu=tuple(map(int,v.outer.split(',')));args=(v.m,v.a,v.t,v.n,mu);lam,nu=physical(*args)
 out={'statement':'G-039','partition':lam,'coefficient':coefficient(*args)}
 if v.polytopes:out['polytopes']=module_polytopes(v.m,v.a,nu)
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
