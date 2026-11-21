#!/usr/bin/env python3
"""Independent exact checks of HD-ALT05; no author code imported."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,time
import sympy as s
started=time.monotonic()
def parts(n,cap=None):
    if n==0: yield ();return
    for x in range(min(n,cap or n),0,-1):
        for y in parts(n-x,x):yield (x,)+y
n,k,x=s.symbols('n k x')
Smax=(n-k-1)*(n-k)*(2*(n-k)-1)/6+k*(k+1)*(2*k+1)/6
u=3*(Smax-n*(n-1)/2)/(n*(n-1)*(n-2))
assert s.simplify((1-u)/3-k*(n-1-k)/((n-1)*(n-2)))==0
tmax=n*(n-1)/2-k*(n-k+1)
assert s.simplify(tmax.subs(k,n/7)-n*(37*n-63)/98)==0
den=12*2401*(n-1)*(n-2)*(n-3)
vb=(37*n-63)**2/(2401*(n-1)*(n-2))+4/((n-2)*(n-3))
poly=379*n**3+4386*n*n-145831*n+157290
assert s.simplify((s.Rational(7,12)-vb)*den-poly)==0
assert s.expand(poly.subs(n,15+x))==379*x**3+21441*x*x+241574*x+235800
assert s.expand(n*(6*n-7)-6*(n-1)*(n-2))==11*n-12
assert F(6,49)>F(5,48)
assert 6/(1+10*F(5,48)-2)==144
assert 2*F(15**3,27)==250
count=0; eligible=0
for N in range(15,31):
 for K in range(1,(N-1)//4+1):
  for tail in parts(K):
   lam=(N-K,)+tail;count+=1
   cs=[j-i for i,r in enumerate(lam) for j in range(r)]
   T=sum(cs);S=sum(c*c for c in cs)
   assert S<=sum(j*j for j in range(1,N-K))+sum(j*j for j in range(1,K+1))
   assert 0<F(N*(N-2*K-1),2)<=T<=N*(N-1)//2-K*(N-K+1)
   U=F(3*(S-N*(N-1)//2),N*(N-1)*(N-2))
   V=F(4*(T*T+N*(N-1)-3*S),N*(N-1)*(N-2)*(N-3))
   assert (1-U)/3>=F(K*(N-1-K),(N-1)*(N-2))
   if 7*K>=N:
    eligible+=1
    assert (1-U)/3>F(6,49)
    assert V<F(7,12)
    assert min((1-U)/3,(1-V)/4)>F(5,48)
proof=Path(__file__).resolve().parents[3]/'research/ordinary_alternating_long_row_obstruction.tex'
out={'status':'PASS','proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'author_code_imported':False,'scope':'independent symbolic identities and all long-row tails for n15..30; universal proof separately audited',
 'all_long_row_tails':count,'newly_excluded_tails':eligible,'n_range':[15,30],
 'source_degree_upper_bound':144,'factor_degree_lower_bound':250,
 'seconds':round(time.monotonic()-started,6)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
