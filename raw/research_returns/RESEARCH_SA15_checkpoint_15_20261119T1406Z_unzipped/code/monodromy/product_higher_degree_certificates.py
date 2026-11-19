#!/usr/bin/env python3
"""Explore the same exact certificates in higher degrees on fixed E x E/F2.
Every retained output is checked; no uniform-in-degree theorem is assumed.
"""
import json,random,time,sys,itertools
from pathlib import Path
import sympy as sp
started=time.perf_counter();base=Path(__file__).resolve().parents[1]
lib=Path(__file__).with_name('product_char2_group_certificates.py')
ns={'__file__':str(lib)}
exec(compile(lib.read_text().split('# Check the custom characteristic')[0],str(lib),'exec'),ns)
rank,apply,charpoly,pdiv,irreducible,reciprocal,pstr,line_certificate=[ns[x] for x in
 ['rank','apply','charpoly','pdiv','irreducible','reciprocal','pstr','line_certificate']]
mul,cartier,deriv=[ns['ns'][x] for x in ['mul','cartier','deriv']]
fieldmul=ns['fieldmul']

def poly_power(a,n,f):
 z=1
 while n:
  if n&1:z=fieldmul(z,a,f)
  a=fieldmul(a,a,f);n>>=1
 return z

d=int(sys.argv[1]) if len(sys.argv)>1 else 3
rng=random.Random(2026111900+d)
B=[(i,0) for i in range(3*d//2+1)]+[(i,1) for i in range((3*d-3)//2+1)]
assert len(B)==3*d
bi={b:i for i,b in enumerate(B)};m=len(B);n=m*m;T=list(itertools.product(range(m),repeat=2))
single=[]
for a in range(m):
 single.append([[bi[z] for z in cartier(mul({B[a]},{B[b]}))] for b in range(m)])
MS=[]
for a,b in T:
 MS.append([sum(1<<(m*i+j) for i in single[a][u] for j in single[b][v]) for u,v in T])
def matrix(s):
 C=[0]*n
 while s:
  j=(s&-s).bit_length()-1;s&=s-1
  C=[a^b for a,b in zip(C,MS[j])]
 return C

D=[]
if d%2==0:
 for side in (0,1):
  cols=[]
  for a,b in T:
   z=0
   for term in deriv({B[(a,b)[side]]}):
    ab=(bi[term],b) if side==0 else(a,bi[term]);z^=1<<(m*ab[0]+ab[1])
   cols.append(z)
  D.append(cols)
 def comps(s):
  out=[]
  for a,b in itertools.product((0,1),repeat=2):
   w=apply(D[0],s) if a else s^apply(D[0],s)
   w=apply(D[1],w) if b else w^apply(D[1],w)
   out.append(w)
  return out

N=n-(4 if d%2==0 else 1)
print('degree',d,'W',n,'nontrivial dimension',N,flush=True)
factor_M=sp.factorint(2**N-1)
primitive_primes=[int(p) for p in factor_M if sp.isprime(p) and sp.n_order(2,p)==N]
print('primitive primes',primitive_primes,flush=True)
assert primitive_primes
out={'degree':d,'W_dimension':n,'basis_E':B,'nontrivial_dimension':N,
 'seed':2026111900+d,'primitive_primes':primitive_primes,
 'scope':'Higher-degree finite certificates, structural conclusion requires external proof'}
dest=base/'outputs'/('product_degree'+str(d)+'_certificates.json')
def save():
 out['runtime_seconds']=time.perf_counter()-started
 dest.write_text(json.dumps(out,indent=2)+'\n')

for attempt in range(1,20001):
 s=rng.getrandbits(n);C=matrix(s)
 if rank(C)!=n:continue
 cp=charpoly(C);f,rem=pdiv(cp,17 if d%2==0 else 3)
 assert not rem
 if irreducible(f) and reciprocal(f)!=f:
  primes=[p for p in primitive_primes if poly_power(2,(2**N-1)//p,f)!=1]
  if primes:
   out['irreducible_frobenius']={'section_bits':s,'columns':C,'attempt':attempt,
    'factor_bits':f,'factor':pstr(f),'primitive_prime_dividing_order':primes[0]}
   print('irreducible Frobenius found',attempt,flush=True);save();break
else:raise AssertionError('No irreducible Frobenius in finite search')

if d%2==0:
 for attempt in range(1,200001):
  s=rng.getrandbits(n);C=matrix(s)
  if rank(C)!=n:continue
  cs=comps(s)
  assert rank(cs)==4 and all(apply(C,v)==v for v in cs)
  im=[C[j]^(1<<j) for j in range(n)]+[s];r=rank(im)
  if rank(im+cs)==r:
   out['no_complement_frobenius']={'section_bits':s,'columns':C,'character_components':cs,
      'attempt':attempt,'image_rank':r,'rank_with_components':r}
   print('no complement Frobenius found',attempt,flush=True);save();break
 else:raise AssertionError('No complement certificate absent in search')
else:
 # A tensor of sections (1+x) times reduced divisors chosen by search
 # provides a second polynomial; any unequal ordinary point suffices.
 for attempt in range(1,1000):
  s=rng.getrandbits(n);C=matrix(s)
  if rank(C)!=n:continue
  f,rem=pdiv(charpoly(C),3);assert not rem
  if f!=out['irreducible_frobenius']['factor_bits']:
   out['different_frobenius']={'section_bits':s,'columns':C,'relative_factor_bits':f};save();break

tested=0
for attempt in range(1,5001):
 a=rng.getrandbits(n);b=rng.getrandbits(n);A=matrix(a);Bmat=matrix(b)
 if rank(Bmat)!=n:continue
 # Avoid the two rational roots, where low-rank coincidences are common.
 if rank(A)!=n or rank([u^v for u,v in zip(A,Bmat)])!=n:continue
 tested+=1
 yes,cert=line_certificate(A,Bmat)
 if yes:
  cert.update({'section_a_bits':a,'section_b_bits':b,'A_columns':A,'B_columns':Bmat,
     'attempt':attempt,'lines_tested':tested})
  out['line_certificate']=cert
  print('line certificate found',attempt,'tested',tested,flush=True);save();break
 if tested%10==0:
  print('tested lines',tested,'attempt',attempt,flush=True)
  out['line_search_progress']={'attempt':attempt,'tested':tested};save()
else:
 out['line_search_not_completed']=True;save()
print('saved',dest,flush=True)
