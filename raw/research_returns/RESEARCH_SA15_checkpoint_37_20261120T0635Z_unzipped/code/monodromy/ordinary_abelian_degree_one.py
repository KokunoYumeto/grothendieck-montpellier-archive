#!/usr/bin/env python3
"""Exact degree-one ordinary curve on the fixed E x E/F2.
Uses the Cartier polynomial routines from the degree-two certificate;
that certificate is rerun first rather than importing unverified output.
"""
import runpy, itertools, random, json, time
from pathlib import Path
import sympy as sp

started=time.perf_counter()
ns=runpy.run_path(str(Path(__file__).with_name('ordinary_abelian_surface.py')))
mul,cartier,rank=ns['mul'],ns['cartier'],ns['rank']
B=[(0,0),(1,0),(0,1)]; bi={b:i for i,b in enumerate(B)}
T=list(itertools.product(range(3),repeat=2)); ti={a:i for i,a in enumerate(T)}
ec={(a,b):[bi[z] for z in cartier(mul({B[a]},{B[b]}))]
    for a in range(3) for b in range(3)}
u,v,w,z=sp.symbols('u v w z')

def cmatrix(s):
 out=[]
 for a,b in T:
  col=0
  for j,(r,t) in enumerate(T):
   if (s>>j)&1:
    for i in ec[r,a]:
     for k in ec[t,b]: col^=1<<ti[i,k]
  out.append(col)
 return out

def chart(a,b,c):
 if c=='Z': return b*b+a*b+a**3+1,(a,a*a+b),[1,a,b]
 return b+a*b+a**3+b**3,(1+a+b*b,a*a+b),[b,a,1]

def smooth(s):
 out=[]
 for c1,c2 in itertools.product(('Z','Y'),repeat=2):
  e1,d1,b1=chart(u,v,c1);e2,d2,b2=chart(w,z,c2)
  f=sp.expand(sum(b1[a]*b2[b] for j,(a,b) in enumerate(T) if (s>>j)&1))
  g=sp.diff(f,u)*d1[0]+sp.diff(f,v)*d1[1]
  h=sp.diff(f,w)*d2[0]+sp.diff(f,z)*d2[1]
  G=sp.groebner([e1,e2,f,g,h],u,v,w,z,modulus=2,order='grevlex')
  yes=len(G.polys)==1 and G.polys[0].as_expr()==1
  out.append({'charts':[c1,c2],'unit_ideal':yes})
  if not yes:return False,out
 return True,out

attempts=[]
for s in range(1,512):
 C=cmatrix(s)
 if rank(C)!=9:continue
 yes,checks=smooth(s)
 attempts.append({'section_bits':s,'smooth':yes})
 if yes:break
else:raise AssertionError('No ordinary smooth F2 degree-one section found')
pts=[(0,1,1),(1,0,1),(1,1,1),(0,1,0)]
count=sum(sum([P[2],P[0],P[1]][a]*[Q[2],Q[0],Q[1]][b]
                  for j,(a,b) in enumerate(T) if (s>>j)&1)%2==0
          for P,Q in itertools.product(pts,repeat=2))
trace=sum((C[i]>>i)&1 for i in range(9))%2
assert count%2==trace
result={'field':'F2','elliptic_curve':'Y^2 Z + X Y Z + X^3 + Z^3=0',
 'ambient':'E x E with Segre L=O(3O) box O(3O)','degree':1,
 'basis':['Z','X','Y'],'section_bits':s,
 'section_terms':[[a,b] for j,(a,b) in enumerate(T) if (s>>j)&1],
 'Cartier_columns_binary':C,'Cartier_rank':9,'relative_rank':8,
 'genus':10,'p_rank':10,'smoothness_certificates':checks,
 'point_count_F2':count,'Cartier_trace_W':trace,'attempts':attempts,
 'runtime_including_degree_two_check':time.perf_counter()-started}
dest=Path(__file__).resolve().parents[1]/'outputs'/'ordinary_abelian_degree_one.json'
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
