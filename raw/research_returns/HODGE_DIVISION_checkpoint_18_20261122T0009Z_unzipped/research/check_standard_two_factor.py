"""Root exact grid-orbit supplement; universal proof remains separate."""
from pathlib import Path
from collections import Counter
from itertools import combinations_with_replacement
from fractions import Fraction
from math import gcd,lcm
from datetime import datetime,timezone
import hashlib,json,time
R=Path(__file__).resolve().parent;start=time.perf_counter()
def parts(n,low=1):
 if n==0:yield ()
 for j in range(low,n+1):
  for rest in parts(n-j,j):yield (j,)+rest
def letters(p,L):
 out=Counter()
 for d,m in Counter(p).items():
  for j in range(d):out[j*(L//d)]+=m
 return out
def grid(p,q,L):
 out=Counter()
 for d,m in Counter(p).items():
  for f,k in Counter(q).items():
   length=lcm(d,f);number=gcd(d,f)*m*k
   for j in range(length):out[j*(L//length)]+=number
 return out
totals={'partition_pairs':0,'tensor_spectral_entries':0,'low_index_one_cases':0,'low_index_minus_one_cases':0,'weighted_swaps':0}
examples=[]
for n in range(15,19):
 a=n-1;e=a*a;rows=0;minimum=None;witness=None
 for p,q in combinations_with_replacement(list(parts(n)),2):
  k=2*n-len(p)-len(q)
  if k==0:continue
  L=lcm(*p,*q);P=letters(p,L);Q=letters(q,L);G=grid(p,q,L)
  G.subtract(P);G.subtract(Q);G[0]+=1
  assert min(G.values())>=0 and sum(G.values())==e
  nu=e-max(G.values());gap=2*nu-((n-3)*k+n)
  assert gap>=0
  c=len(p);d=len(q)
  U=P.copy();U[0]-=1;V=Q.copy();V[0]-=1
  assert sum(z*z for z in U.values())<=(n-2)*c+1
  assert sum(z*z for z in V.values())<=(n-2)*d+1
  assert 2*nu>=(n-2)*k
  if k<n:
   kx=n-c;ky=n-d
   gap_grid=Fraction(n*(c+d),2)-sum(gcd(x,y) for x in p for y in q)
   assert gap_grid>=Fraction(Counter(q)[1]*kx+Counter(p)[1]*ky,2)>=Fraction(k*(n-k),2)
   assert e-G[0]==Fraction((n-2)*k,2)+gap_grid
   totals['low_index_one_cases']+=1
   if L%2==0:
    Cminus=sum(gcd(x,y) for x in p for y in q if lcm(x,y)%2==0)
    u=sum(x%2 for x in p);v=sum(x%2 for x in q)
    H=Fraction(n*(c+d),2)-Cminus
    assert H>=Fraction(u*d+v*c,2)
    margin=H-u-v+1
    assert margin>=Fraction(n-k,2)
    assert e-G[L//2]==Fraction((n-2)*k,2)+margin
    totals['low_index_minus_one_cases']+=1
  if minimum is None or gap<minimum:minimum=gap;witness=[p,q]
  rows+=1;totals['tensor_spectral_entries']+=len(+G)
 totals['partition_pairs']+=rows
 examples.append({'n':n,'pairs':rows,'minimum_twice_gap':minimum,'witness':witness})
# A separate direct eigenbasis-word construction for weighted swaps.
for n in range(15,23):
 a=n-1;e=a*a
 for p in parts(n):
  L=lcm(*p);U=letters(p,L);U[0]-=1;vals=list((+U).elements());S=Counter()
  for i,x in enumerate(vals):
   S[2*x]+=1
   for y in vals[i+1:]:S[(x+y)%(2*L)]+=1;S[(x+y+L)%(2*L)]+=1
  assert sum(S.values())==e
  rank=e-max(S.values());index=n-len(p)
  assert 2*rank>=e-a and 2*rank>=e+a*index-2*a
  totals['weighted_swaps']+=1
arithmetic=[]
for n in (15,16,20,100,1000,1000000):
 a=n-1;e=a*a;A=Fraction(n-3,2);B=Fraction(n,2)
 assert Fraction(a,2)-A==1
 assert e+A*(2*a)+10*B-2*a==2*e+a+5
 assert a+5>6 and 6*a>6 and e>=B
 beta=Fraction(1,n-1)
 if n==100:assert beta<Fraction(1,10)+Fraction(3,5*e)
 arithmetic.append({'n':n,'e':e,'excess_over_2e':a+5})
proof=R/'alternating_standard_two_factor_section.tex'
out={'status':'PASS','completed_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'counts':totals,'examples':examples,'arithmetic':arithmetic,
 'scope':'Root actual grid-cycle eigenspaces, Cauchy sums, low-index real-target margins and direct weighted words. Finite supplement only; arbitrary n, actual normalizer and connected-cover RH are proved in the separate full text.'}
(R/'standard_two_factor_checked.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
