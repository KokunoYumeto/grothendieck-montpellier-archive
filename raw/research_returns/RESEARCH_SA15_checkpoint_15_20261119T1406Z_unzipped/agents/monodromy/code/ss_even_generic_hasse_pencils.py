#!/usr/bin/env python3
"""Exact generic-pencil variant of the retained degree-two unit-Hasse probe.

The kernel minor p(t) is allowed to move.  If Ntilde is the denominator-cleared
33x33 quotient matrix, h(t)=det(Ntilde)/p(t)^65.  Every division is verified.
This file does not infer a global theorem from the displayed factorization.
"""
from pathlib import Path
source=Path(__file__).with_name('ss_even_unit_hasse_pencils.py').read_text()
exec(compile(source.split('for trial in range(6):')[0],'<retained exact Cartier helpers>','exec'))
started=time.perf_counter();records=[];rng=random.Random(248681505)
def pdet3(P):
 return pmul(P[0][0],pmul(P[1][1],P[2][2])^pmul(P[1][2],P[2][1]))^pmul(P[0][1],pmul(P[1][0],P[2][2])^pmul(P[1][2],P[2][0]))^pmul(P[0][2],pmul(P[1][0],P[2][1])^pmul(P[1][1],P[2][0]))
def ppow(a,e):
 z=1
 while e:
  if e&1:z=pmul(z,a)
  a=pmul(a,a);e>>=1
 return z
for trial in range(4):
 s1=rng.randrange(1,1<<36);U1=[s1,dbits(s1,0),dbits(s1,1)]
 U=[[((U0[j]>>i)&1)|(((U1[j]>>i)&1)<<1) for j in range(3)] for i in range(n)]
 P=[U[i] for i in R];p=pdet3(P);assert p&1
 adj=[[0]*3 for _ in range(3)]
 for i,j in itertools.product(range(3),repeat=2):
  rs=[a for a in range(3) if a!=j];cs=[a for a in range(3) if a!=i]
  adj[i][j]=pmul(P[rs[0]][cs[0]],P[rs[1]][cs[1]])^pmul(P[rs[0]][cs[1]],P[rs[1]][cs[0]])
 for i,j in itertools.product(range(3),repeat=2):
  z=0
  for a in range(3):z^=pmul(P[i][a],adj[a][j])
  assert z==(p if i==j else 0)
 UA=[[0]*3 for _ in range(n)]
 for i,j in itertools.product(range(n),range(3)):
  for a in range(3):UA[i][j]^=pmul(U[i][a],adj[a][j])
 C1=matrix(s1);M=[[C0[i][j]|(C1[i][j]<<1) for j in range(n)] for i in range(n)]
 N=[]
 for i in J:
  row=[]
  for j in J:
   z=pmul(psquare(p),M[i][j])
   for a,r in enumerate(R):z^=pmul(psquare(UA[i][a]),M[r][j])
   row.append(z)
  N.append(row)
 numerator=det(N);h=pdiv(numerator,ppow(p,65));assert h&1 and h.bit_length()<=37
 poly=sp.Poly(sum(((h>>i)&1)*t**i for i in range(h.bit_length())),t,modulus=2)
 factors=sp.factor_list(poly)[1]
 records.append({'trial':trial,'s0_bits':s0,'s1_bits':s1,'pivot_rows':R,'kernel_minor_bits':p,
 'polynomial_bits':h,'degree':poly.degree(),'factors':[{'polynomial':str(f.as_expr()),'degree':f.degree(),'multiplicity':e} for f,e in factors],
 'derivative_gcd_degree':sp.gcd(poly,poly.diff()).degree(),'squarefree':sp.gcd(poly,poly.diff()).degree()==0})
out={'status':'PASS','scope':'four exact generic degree-two unit-image Hasse pencils; no global conclusion in this script',
 'method':'moving kernel minor p; polynomial determinant divided exactly by p^65',
 'records':records,'runtime_seconds':time.perf_counter()-started}
Path(__file__).resolve().parents[1].joinpath('outputs/ss_even_generic_hasse_pencils.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
