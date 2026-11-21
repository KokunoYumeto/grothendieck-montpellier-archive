#!/usr/bin/env python3
"""Exact binary-quartic presentation, SAGBI, and plethysm checks."""
from pathlib import Path
from itertools import combinations
import csv
import sympy as s

x=s.symbols('x0:5')
f=x[0]
H=x[0]*x[2]-x[1]**2
T=x[0]**2*x[3]-3*x[0]*x[1]*x[2]+2*x[1]**3
I=x[0]*x[4]-4*x[1]*x[3]+3*x[2]**2
J=x[0]*x[2]*x[4]+2*x[1]*x[2]*x[3]-x[0]*x[3]**2-x[1]**2*x[4]-x[2]**3
gens={'f':f,'H':H,'T':T,'I':I,'J':J}
def D(p):
 return s.expand(sum(i*x[i-1]*s.diff(p,x[i]) for i in range(1,5)))
for name,p in gens.items(): assert D(p)==0,(name,D(p))
assert s.expand(T**2+4*H**3-f**2*H*I+f**3*J)==0
weights=(1,2,1,2,2)
expected={'f':(1,0,0,0,0),'H':(0,2,0,0,0),'T':(0,3,0,0,0),'I':(0,1,0,1,0),'J':(0,2,0,0,1)}
receipts=[]
for name,p in gens.items():
 terms=s.Poly(p,*x).terms()
 lead=max(terms,key=lambda t:(sum(a*b for a,b in zip(weights,t[0])),t[0]))
 assert lead[0]==expected[name],(name,lead)
 receipts.append(f'{name}: weighted leading term {lead}')
obstruction=s.expand(f*J-H*I)
lexlead=s.Poly(obstruction,*x).terms()[0]
assert lexlead[0]==(2,0,0,2,0)
receipts.append(f'Lex obstruction fJ-HI={obstruction}; leading term {lexlead}')
N=100
# Independent positive count from the free module with T exponent zero or one.
counts=[[0]*(4*N+1) for _ in range(N+1)]
counts[0][0]=1
for degree,k in ((1,0),(2,2),(2,4),(3,6)):
 for n in range(degree,N+1):
  for j in range(k,4*N+1):
   counts[n][j]+=counts[n-degree][j-k]
basis=[[counts[n][j]+(counts[n-3][j-3] if n>=3 and j>=3 else 0) for j in range(4*N+1)] for n in range(N+1)]
# Weight count for 4 by n partitions, via the Gaussian product with 16 terms.
p=[0]*(2*N+1)
p[0]=1
for part in range(1,5):
 for j in range(part,2*N+1):p[j]+=p[j-part]
rows=[]
for n in range(N+1):
 shifts=[(sum(n+i for i in S),(-1)**len(S)) for r in range(5) for S in combinations(range(1,5),r)]
 def rect(j):
  return sum(sign*p[j-shift] for shift,sign in shifts if 0<=j-shift<=2*N)
 for k in range(2*n+1):
  independent=rect(k)-rect(k-1)
  assert basis[n][k]==independent,(n,k,basis[n][k],independent)
  rows.append((n,4*n-k,k,basis[n][k],independent))
out=Path(__file__).parent
with (out/'BINARY_QUARTIC_CHECK.tsv').open('w',newline='') as fp:
 w=csv.writer(fp,delimiter='\t');w.writerow(('inner_n','lambda1','lambda2','positive_basis_count','independent_weight_difference'));w.writerows(rows)
(out/'SYMBOLIC_CHECK.txt').write_text('\n'.join(receipts)+'\nAll five D derivatives and the defining relation vanish identically.\n')
print(f'PASS: presentation identities, weighted SAGBI leading terms, lex obstruction; {len(rows)} coefficients for n=0..{N}.')

