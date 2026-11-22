#!/usr/bin/env python3
"""Exact discovery and certificates for the supersingular degree-two group.
The first discovery was run read-only during CP10 freeze; this retained
script repeats its deterministic 106-section search and adds witnesses.
All geometry and group implications are proved separately in TeX.
"""
from pathlib import Path
import itertools,random,time,json,sympy as sp
started=time.perf_counter();base=Path(__file__).resolve().parent
ns={'__file__':str(base/'product_char2_group_certificates.py')}
exec(compile((base/'product_char2_group_certificates.py').read_text().split('# Check the custom characteristic')[0],ns['__file__'],'exec'),ns)
charpoly,pdiv,irreducible,reciprocal,pmul,pmod,rank,apply,pstr=[ns[k] for k in ['charpoly','pdiv','irreducible','reciprocal','pmul','pmod','rank','apply','pstr']]
B=[(0,0),(1,0),(2,0),(3,0),(0,1),(1,1)];bi={b:i for i,b in enumerate(B)}
def cart(i,j):
 if not j:return {(i//2,0)} if i%2 else set()
 return {(i//2,1)} if i%2 else {(i//2+1,0)}
def prod(a,b):
 i,j=a;u,v=b
 return {(i+u,j+v)} if j+v<2 else {(i+u,1),(i+u+3,0)}
def cp(a,b):
 out=set()
 for i,j in prod(a,b):out.symmetric_difference_update(cart(i,j))
 return [bi[v] for v in out]
one=[[cp(a,b) for b in B] for a in B];T=list(itertools.product(range(6),repeat=2));n=36
matrices=[[sum(1<<(6*i+j) for i in one[a][u] for j in one[b][v]) for u,v in T] for a,b in T]
def matrix(s):
 C=[0]*n
 while s:
  q=s&-s;s^=q;C=[a^b for a,b in zip(C,matrices[q.bit_length()-1])]
 return C
delta=[0,1,0,4,4,(1<<3)|(1<<4)]
D=[sum(1<<(6*i+j) for i in range(6) if delta[a]>>i&1 for j in range(6) if delta[b]>>j&1) for a,b in T]
def ppow(a,e,f):
 z=1
 while e:
  if e&1:z=pmod(pmul(z,a),f)
  a=pmod(pmul(a,a),f);e>>=1
 return z
def solve(cols,v):
 piv={}
 for j,c in enumerate(cols):
  u=1<<j
  while c:
   i=c.bit_length()-1
   if i in piv:c^=piv[i][0];u^=piv[i][1]
   else:piv[i]=(c,u);break
 w=0
 while v:
  i=v.bit_length()-1
  assert i in piv
  v^=piv[i][0];w^=piv[i][1]
 return w
rng=random.Random(202611191023);first=second=None
for attempt in range(1,10001):
 s=rng.getrandbits(n);C=matrix(s)
 if rank(C)!=33:continue
 C2=[apply(C,v) for v in C]
 if rank(C2)!=33:continue
 lam=apply(D,s);assert lam and apply(C,lam)==lam
 if second is None:
  image=[c^(1<<j) for j,c in enumerate(C)]
  r=rank(image)
  if rank(image+[lam])==r:
   second={'section_bits':s,'attempt':attempt,'lambda_bits':lam,
           'rank_C_minus_I':r,'full_charpoly_bits':charpoly(C),
           'columns':C,'image_witness_bits':solve(image,lam)}
 if first is None:
  cp0=charpoly(C);assert cp0&7==0
  f,rem=pdiv(cp0>>3,3);assert rem==0
  if irreducible(f) and reciprocal(f)!=f:
   has=ppow(2,((1<<32)-1)//65537,f)!=1
   if has:first={'section_bits':s,'attempt':attempt,'lambda_bits':lam,
                 'kernel_polynomial_bits':f,'kernel_polynomial':pstr(f),
                 'primitive_prime':65537,'columns':C,'full_charpoly_bits':cp0}
 if first and second:break
assert attempt==106 and first['section_bits']==60944792081 and second['section_bits']==1642027529
assert first['kernel_polynomial_bits']==4853921047
for rec in (first,second):
 C=rec['columns'];rec['rank_C']=rank(C);rec['rank_C2']=rank([apply(C,v) for v in C])
 assert rec['rank_C']==rec['rank_C2']==33
 t=sp.Symbol('T');integer=sp.Matrix(36,36,lambda i,j:(C[j]>>i)&1).charpoly(t).as_poly()
 exact=sum((int(c)%2)<<m[0] for m,c in integer.terms())
 assert exact==rec['full_charpoly_bits'];rec['integer_charpoly_independent_check']=True
assert apply([c^(1<<j) for j,c in enumerate(second['columns'])],second['image_witness_bits'])==second['lambda_bits']
assert all(65537%j for j in range(2,257))
assert pow(2,32,65537)==1 and pow(2,16,65537)!=1
out={'status':'PASS','curve':'y^2+y=x^3','line_bundle':'O(6O) external O(6O)',
 'basis':B,'tensor_index':'6*i+j; bit0 is (1,1)',
 'matrix_convention':'C is root-removed Cartier multiplication on W; coherent Frobenius matrix is transpose(C)',
 'seed':202611191023,'attempts':attempt,'irreducible_kernel_frobenius':first,
 'no_fixed_quotient_lift_frobenius':second,'runtime_seconds':time.perf_counter()-started}
Path(__file__).resolve().parents[1].joinpath('outputs/supersingular_product_degree_two.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('irreducible_kernel_frobenius','no_fixed_quotient_lift_frobenius')},indent=2))
print(json.dumps({'first':{k:v for k,v in first.items() if k!='columns'},'second':{k:v for k,v in second.items() if k!='columns'}},indent=2))
