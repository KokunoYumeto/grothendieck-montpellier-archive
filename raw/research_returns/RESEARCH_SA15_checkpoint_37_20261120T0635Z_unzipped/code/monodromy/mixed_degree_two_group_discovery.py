#!/usr/bin/env python3
"""Retained exact discovery for the generic mixed-product degree-two gate.

Special coefficient fibre: Eo:y²+xy=x³+1, Es:y²+y=x³ over F2.
The theorem using these points must separately justify generic-family normality.
"""
import itertools,json,random,time
from pathlib import Path
import sympy as sp
started=time.perf_counter();basis=[(0,0),(1,0),(2,0),(3,0),(0,1),(1,1)];idx={a:i for i,a in enumerate(basis)}
def cart(a,b,ordinary):
 u,v=a[0]+b[0],a[1]+b[1]
 terms=[(u,v)] if v<2 else ([(u+1,1),(u+3,0),(u,0)] if ordinary else [(u,1),(u+3,0)])
 out=0
 for u,v in terms:
  if ordinary:
   if v:
    targets=[(u//2+1,0)] if u%2==0 else [(u//2,1),(u//2,0)]
   else:targets=[] if u%2 else [(u//2,0)]
  else:
   if v:targets=[(u//2,1)] if u%2 else [(u//2+1,0)]
   else:targets=[(u//2,0)] if u%2 else []
  for target in targets:out^=1<<idx[target]
 return out
def deriv(a,ordinary):
 u,v=a;out=0
 if ordinary:
  if (u+v)%2:out^=1<<idx[(u,v)]
  if v:out^=1<<idx[(u+2,0)]
 else:
  if u%2:out^=1<<idx[(u-1,v)]
  if v:out^=1<<idx[(u+2,0)]
 return out
ct=[[[cart(a,b,o) for b in basis] for a in basis] for o in (True,False)]
dt=[[deriv(a,o) for a in basis] for o in (True,False)]
coef=[];do=[];ds=[]
for a,b in itertools.product(range(6),repeat=2):
 rows=[0]*36
 for u,v in itertools.product(range(6),repeat=2):
  for i,j in itertools.product(range(6),repeat=2):
   if (ct[0][a][u]>>i)&1 and (ct[1][b][v]>>j)&1:rows[6*i+j]^=1<<(6*u+v)
 coef.append(rows)
 do.append(sum(((dt[0][a]>>i)&1)<<(6*i+b) for i in range(6)))
 ds.append(sum(((dt[1][b]>>j)&1)<<(6*a+j) for j in range(6)))
def apply_columns(cols,v):
 z=0
 while v:
  bit=v&-v;z^=cols[bit.bit_length()-1];v^=bit
 return z
def rebuild(s):
 rows=[0]*36;v=s
 while v:
  bit=v&-v;j=bit.bit_length()-1;rows=[a^b for a,b in zip(rows,coef[j])];v^=bit
 return rows
def rref(rows,width=36):
 rows=rows[:];r=0;piv=[]
 for j in range(width):
  k=next((i for i in range(r,len(rows)) if (rows[i]>>j)&1),None)
  if k is None:continue
  rows[r],rows[k]=rows[k],rows[r]
  for i in range(len(rows)):
   if i!=r and (rows[i]>>j)&1:rows[i]^=rows[r]
  piv.append(j);r+=1
 return rows,piv
def rank(rows):return len(rref(rows)[1])
def square(rows):return [apply_columns(rows,row) for row in rows]
def matvec(rows,v):return sum(((row&v).bit_count()%2)<<i for i,row in enumerate(rows))
def solve_two(rows,ls):
 rr=[row|(((ls[0]>>i)&1)<<36)|(((ls[1]>>i)&1)<<37) for i,row in enumerate(rows)]
 rr,piv=rref(rr);r=len(piv)
 if any(row>>36 for row in rr[r:]):return None
 return [sum(((row>>(36+a))&1)<<j for row,j in zip(rr,piv)) for a in range(2)]
def pmod(a,f):
 while a.bit_length()>=f.bit_length():a^=f<<(a.bit_length()-f.bit_length())
 return a
def psquare(a):return sum(((a>>i)&1)<<(2*i) for i in range(a.bit_length()))
def pgcd(a,b):
 while b:a,b=b,pmod(a,b)
 return a
def irreduc32(f):
 if f.bit_length()!=33:return False
 x=2
 for i in range(1,33):
  x=pmod(psquare(x),f)
  if i==16 and pgcd(x^2,f)!=1:return False
 return x==2
rng=random.Random(248681506);records={};counts={'tested':0,'maximal_rank':0,'charpolys':0};T=sp.Symbol('T')
for trial in range(1,20001):
 s=rng.randrange(1,1<<36);C=rebuild(s);counts['tested']+=1
 if rank(C)!=34 or rank(square(C))!=34:continue
 counts['maximal_rank']+=1
 l0=apply_columns(ds,s);l1=apply_columns(do,l0)
 assert l0 and l1 and l0!=l1 and matvec(C,l0)==l0 and matvec(C,l1)==l1
 if 'translation' not in records:
  mus=solve_two([row^(1<<i) for i,row in enumerate(C)],[l0,l1])
  if mus is not None:
   assert all(matvec(C,mu)^mu==lam for mu,lam in zip(mus,[l0,l1]))
   records['translation']={'section_bits':s,'lambda_bits':[l0,l1],'mu_bits':mus,'rank_C':34,'rank_C2':34,'rank_C_minus_I':rank([row^(1<<i) for i,row in enumerate(C)]),'trial':trial}
 if 'irreducible' not in records:
  M=sp.Matrix(36,36,lambda i,j:(C[i]>>j)&1);cp=sp.Poly(M.charpoly(T).as_expr(),T,modulus=2)
  f,rem=sp.div(cp,sp.Poly(T**2*(T+1)**2,T,modulus=2));assert rem.is_zero
  fb=sum((int(v)%2)<<mon[0] for mon,v in f.terms());counts['charpolys']+=1
  if irreduc32(fb) and fb!=sum(((fb>>i)&1)<<(32-i) for i in range(33)):
   records['irreducible']={'section_bits':s,'lambda_bits':[l0,l1],'kernel_polynomial_bits':fb,'kernel_polynomial':str(f.as_expr()),'full_charpoly':str(cp.as_expr()),'rank_C':34,'rank_C2':34,'irreducible':True,'nonreciprocal':True,'trial':trial}
 if len(records)==2:break
out={'status':'PASS' if len(records)==2 else 'NOT_FOUND','curves':['y²+xy=x³+1','y²+y=x³'],'basis':basis,'counts':counts,'records':records,'runtime_seconds':time.perf_counter()-started}
Path(__file__).resolve().parents[1].joinpath('outputs/mixed_degree_two_group_discovery.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
