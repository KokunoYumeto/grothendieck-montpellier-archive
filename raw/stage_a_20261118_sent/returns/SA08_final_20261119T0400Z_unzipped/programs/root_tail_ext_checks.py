"""Finite checks for the characteristic-p Frobenius argument; not an arbitrary-base proof."""
from math import comb
import json
rows=[]
for p,r in [(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(5,0),(5,1)]:
 N=p**(r+1);D=N-1
 pair=[comb(D,a)%p for a in range(N)]
 assert all(pair)
 overflow=[(a,b) for a in range(N) for b in range(N) if a+b>=N]
 assert all(comb(a+b,a)%p==0 for a,b in overflow)
 rows.append({'p':p,'r':r,'rank':N,'top_degree':D,'pairing_coefficients':pair,'overflow_products_zero':len(overflow)})
print(json.dumps({'finite_Frobenius_checks':rows,'result':'all passed','scope':'k is an F_p-algebra; proof with arbitrary M and fixed internal degree in root/tail_ext_restricted_proof.md'},indent=2))
