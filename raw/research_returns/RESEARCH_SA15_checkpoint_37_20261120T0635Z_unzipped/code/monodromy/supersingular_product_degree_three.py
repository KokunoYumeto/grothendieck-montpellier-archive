#!/usr/bin/env python3
"""Bounded exact Frobenius search for ss product degree three; proof external."""
from pathlib import Path
import itertools,random,time,json,sympy as sp
started=time.perf_counter();base=Path(__file__).resolve().parent
ns={'__file__':str(base/'product_char2_group_certificates.py')}
exec(compile((base/'product_char2_group_certificates.py').read_text().split('# Check the custom characteristic')[0],ns['__file__'],'exec'),ns)
charpoly,irreducible,reciprocal,pmul,pmod,rank,apply,pstr=[ns[k] for k in ['charpoly','irreducible','reciprocal','pmul','pmod','rank','apply','pstr']]
m=9;n=m*m;B=[(i,0) for i in range(5)]+[(i,1) for i in range(4)];bi={b:i for i,b in enumerate(B)}
def cprod(a,b):
 i=a[0]+b[0];j=a[1]+b[1];P=[(i,j)] if j<2 else [(i,1),(i+3,0)];ans=set()
 for u,v in P:
  if not v:
   if not u%2:continue
   z=(u//2,0)
  else:z=(u//2,1) if u%2 else (u//2+1,0)
  if z in ans:ans.remove(z)
  else:ans.add(z)
 return [bi[z] for z in ans]
one=[[cprod(a,b) for b in B] for a in B];T=list(itertools.product(range(m),repeat=2))
matrices=[[sum(1<<(m*i+j) for i in one[a][u] for j in one[b][v]) for u,v in T] for a,b in T]
def matrix(s):
 C=[0]*n
 while s:
  q=s&-s;s^=q;C=[a^b for a,b in zip(C,matrices[q.bit_length()-1])]
 return C
def ppow(a,e,f):
 z=1
 while e:
  if e&1:z=pmod(pmul(z,a),f)
  a=pmod(pmul(a,a),f);e>>=1
 return z
rng=random.Random(202611191030);found=None;ordinary=0
for attempt in range(1,10001):
 s=rng.getrandbits(n);C=matrix(s)
 if rank(C)!=80 or rank([apply(C,v) for v in C])!=80:continue
 ordinary+=1;cp=charpoly(C);assert cp&1==0
 f=cp>>1
 if irreducible(f) and reciprocal(f)!=f and ppow(2,((1<<80)-1)//4278255361,f)!=1:
  found={'section_bits':s,'attempt':attempt,'rank_C':80,'rank_C2':80,
   'full_charpoly_bits':cp,'polynomial_bits':f,'polynomial':pstr(f),
   'primitive_prime':4278255361,'columns':C};break
assert found is not None
assert all(4278255361%j for j in range(2,65599))
assert pow(2,80,4278255361)==1 and pow(2,40,4278255361)!=1 and pow(2,16,4278255361)!=1
Z=sp.Symbol('T');P=sp.Matrix(81,81,lambda i,j:(C[j]>>i)&1).charpoly(Z).as_poly()
ref=sum((int(c)%2)<<int(a[0]) for a,c in P.terms());assert ref==found['full_charpoly_bits']
found['independent_integer_charpoly_check']=True
out={'status':'PASS','degree':3,'basis':B,'tensor_index':'9*i+j',
 'seed':202611191030,'maximal_rank_points_tested':ordinary,'certificate':found,
 'runtime_seconds':time.perf_counter()-started}
Path(__file__).resolve().parents[1].joinpath('outputs/supersingular_product_degree_three.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='certificate'},indent=2));print(json.dumps({k:v for k,v in found.items() if k!='columns'},indent=2))
