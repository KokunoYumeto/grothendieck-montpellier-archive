"""G037: uniform positive stable-hook Schur plethysm, all outer degrees.

Sparse integer polytope matrices are returned as named variables and
rows {coefficients, relation, rhs}. No character oracle is used here.
"""
from functools import lru_cache
from itertools import combinations
import argparse,json

def trim(p):
 p=list(p)
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def mul(p,q):
 z=[0]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  if a:
   for j,b in enumerate(q):
    if b:z[i+j]+=a*b
 return trim(z)
def rational_coefficient(p,q,n):
 """Exact Bostan--Mori parity extraction; valid for every n>=0."""
 if n<0:return 0
 p=trim(p);q=trim(q)
 while n:
  qm=[a*(-1)**i for i,a in enumerate(q)]
  s=mul(p,qm);t=mul(q,qm)
  p=trim(s[n%2::2] or [0]);q=trim(t[::2]);n//=2
 assert p[0]%q[0]==0
 return p[0]//q[0]
def denominator(lo,hi):
 z=[1]
 for i in range(lo,hi+1):z=mul(z,[1]+[0]*(i-1)+[-1])
 return z
def transpose(lam):
 return tuple(sum(a>=i for a in lam) for i in range(1,lam[0]+1))
def cells(lam):return tuple((i,j) for i,a in enumerate(lam,1) for j in range(1,a+1))
def valid_partition(lam,m):
 return bool(lam) and sum(lam)==m and all(type(a)is int and a>0 for a in lam) and all(lam[i]>=lam[i+1] for i in range(len(lam)-1))
@lru_cache(None)
def fake_degree(lam):
 m=sum(lam);N=m*(m-1)//2;b=sum(i*a for i,a in enumerate(lam));tr=transpose(lam)
 z=[1]+[0]*N
 for j in range(1,m+1):
  for k in range(N,j-1,-1):z[k]-=z[k-j]
 for i,j in cells(lam):
  h=lam[i-1]-j+tr[j-1]-i+1
  for k in range(h,N+1):z[k]+=z[k-h]
 z=trim(([0]*b+z)[:N+1])
 assert all(a>=0 for a in z)
 return tuple(z)
def elementary(weights,r):
 e=[{0:1}]+[{} for _ in range(r)]
 for w in weights:
  for k in range(r,0,-1):
   for d,a in list(e[k-1].items()):e[k][d+w]=e[k].get(d+w,0)+a
 return e[r]
def poly_from_dict(d):
 if not d:return [0]
 assert min(d)>=0
 return [d.get(i,0) for i in range(max(d)+1)]
@lru_cache(None)
def nontrivial_numerator(nu,r):
 w=[j-i+1 for i,j in cells(nu) if (i,j) not in ((1,1),(2,1))]
 e=elementary(w,r);f=fake_degree(nu);out={}
 for i,a in enumerate(f):
  if a:
   for j,b in e.items():out[i+j]=out.get(i+j,0)+a*b
 return tuple(poly_from_dict(out))
def module_coefficient(m,a,r,nu):
 nu=tuple(nu)
 if not(m>=3 and a>=1 and 0<=r<=m-2 and valid_partition(nu,m)):raise ValueError('invalid stable-hook parameters')
 D=a+r
 if nu!=(m,):return rational_coefficient(nontrivial_numerator(nu,r),denominator(2,m),D)
 result=0
 for i in range(2,m+1):
  e=elementary(range(i+1,m+1),r)
  if e:result+=rational_coefficient(poly_from_dict({d+i:v for d,v in e.items()}),denominator(i,m),D)
 return result
def module_support(m,a,r,nu):
 nu=tuple(nu);D=a+r
 if nu==(m,):
  L=(r+2)*(r+3)//2-1
  return D>=L and not(r==m-2 and D==L+1)
 w=sorted(j-i+1 for i,j in cells(nu) if (i,j) not in ((1,1),(2,1)))
 L=sum(i*a for i,a in enumerate(nu))+sum(w[:r])
 rectangular=len(set(nu))==1
 return D>=L and not(D==L+1 and rectangular and r in (0,m-2))
def physical(m,a,r,t,n,mu):
 mu=tuple(mu)
 if any(type(v)is not int for v in (m,a,r,t,n)) or m<3 or a<1 or not 0<=r<=m-2 or t<0 or n<a+t or not valid_partition(mu,m):raise ValueError('invalid stable-hook input')
 A=m*n-a-(m-1)*t-r
 lam=(A,a+t)+(t+1,)*r+(t,)*(m-2-r)
 assert lam[0]>=lam[1] and sum(lam)==m*n
 return lam,transpose(mu) if t%2 else mu
def coefficient(m,a,r,t,n,mu):
 _,nu=physical(m,a,r,t,n,mu)
 return module_coefficient(m,a,r,nu)

class Matrix:
 def __init__(self):self.variables=[];self.rows=[]
 def var(self,name,lo=None,hi=None):
  self.variables.append(name)
  if lo is not None:self.row({name:1},'>=',lo)
  if hi is not None:self.row({name:1},'<=',hi)
  return name
 def row(self,co,relation,rhs):self.rows.append({'coefficients':{k:v for k,v in co.items() if v},'relation':relation,'rhs':rhs})
 def data(self):return {'variables':self.variables,'constraints':self.rows,'variable_count':len(self.variables),'constraint_count':len(self.rows)}
def module_polytope(m,a,r,nu):
 nu=tuple(nu)
 if not(m>=3 and a>=1 and 0<=r<=m-2 and valid_partition(nu,m)):raise ValueError('invalid module parameters')
 D=a+r;P=Matrix()
 if nu==(m,):
  z={j:P.var(f'z{j}',0,1) for j in range(2,m+1)}
  y={j:P.var(f'y{j}',0,1) for j in range(2,m+1)}
  b={j:P.var(f'b{j}',0,D//j) for j in range(2,m+1)}
  P.row({v:1 for v in z.values()},'=',1);P.row({v:1 for v in y.values()},'=',r)
  for j in range(2,m+1):
   P.row({y[j]:1,**{z[i]:-1 for i in range(2,j)}},'<=',0)
   P.row({b[j]:1,z[j]:-1,y[j]:-1},'>=',0)
   P.row({b[j]:1,**{z[i]:-D for i in range(2,j+1)}},'<=',0)
  P.row({b[j]:j for j in b},'=',D)
  return {'branch':'trivial','degree':D,**P.data()}
 C=cells(nu);X={(c,j):P.var(f'X{c[0]}_{c[1]}_{j}',0,1) for c in C for j in range(1,m+1)}
 delta={j:P.var(f'd{j}',0,1) for j in range(1,m)}
 Y={c:P.var(f'Y{c[0]}_{c[1]}',0,1) for c in C if c not in ((1,1),(2,1))}
 coin={j:P.var(f'c{j}',0,(D+m*m)//j) for j in range(2,m+1)}
 for c in C:P.row({X[c,j]:1 for j in range(1,m+1)},'=',1)
 for j in range(1,m+1):P.row({X[c,j]:1 for c in C},'=',1)
 for i,j in C:
  for cp in ((i+1,j),(i,j+1)):
   if cp in C:P.row({**{X[(i,j),k]:k for k in range(1,m+1)},**{X[cp,k]:-k for k in range(1,m+1)}},'<=',-1)
 for j in range(1,m):
  co={**{X[c,j+1]:c[0] for c in C},**{X[c,j]:-c[0] for c in C},delta[j]:-m}
  P.row(co,'>=',1-m);P.row(co,'<=',0)
 P.row({v:1 for v in Y.values()},'=',r)
 P.row({**{coin[j]:j for j in coin},**{delta[j]:m-j for j in delta},**{Y[c]:c[1]-c[0]+1 for c in Y}},'=',D)
 return {'branch':'nontrivial','degree':D,**P.data()}
def polytope(m,a,r,t,n,mu):
 lam,nu=physical(m,a,r,t,n,mu)
 return {'partition':lam,'outer':tuple(mu),'effective_outer':nu,'polytope':module_polytope(m,a,r,nu)}
def valid_witness(data,w):
 if set(w)!=set(data['variables']) or any(type(v)is not int for v in w.values()):return False
 for row in data['constraints']:
  v=sum(c*w[x] for x,c in row['coefficients'].items());b=row['rhs'];op=row['relation']
  if (op=='=' and v!=b) or(op=='<=' and v>b) or(op=='>=' and v<b):return False
 return True
def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('m','a','r','t','n'):p.add_argument('--'+name,type=int,required=True)
 p.add_argument('--outer',required=True);p.add_argument('--polytope',action='store_true');v=p.parse_args();mu=tuple(map(int,v.outer.split(',')));args=(v.m,v.a,v.r,v.t,v.n,mu)
 out={'coefficient':coefficient(*args),'partition':physical(*args)[0]}
 if v.polytope:out.update(polytope(*args))
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
