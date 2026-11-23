#!/usr/bin/env python3
"""Exact nodal degeneration certificate for genus-four cyclic Prym maps.
Uses only polynomial arithmetic over Z; no approximate complex arithmetic.
"""
import json
from pathlib import Path
import sympy as S
z,L=S.symbols('z L')
a=(0,1,2,3); b=(5,7,11,13)
D=S.Poly(S.prod(z-p for p in a+b),z)
quot={p:D.exquo(S.Poly(z-p,z)).as_expr() for p in a+b}
A=[S.expand(quot[a[j]]-quot[a[3]]) for j in range(3)]
B=[S.expand(quot[b[j]]-quot[b[3]]) for j in range(3)]
f=[A[j]-L*B[j] for j in range(3)]
# L times the eta-inverse basis, to keep all coefficients integral.
h=[L*A[j]-B[j] for j in range(3)]
products=[S.Poly(S.expand(f[j]*h[k]),z) for j in range(3) for k in range(3)]
M=S.Matrix([[p.coeff_monomial(z**v) for p in products] for v in range(13)])
minor=M[:9,:]
print('computing polynomial determinant',flush=True)
det=S.factor(minor.det(method='domain-ge'))
print('factored determinant:',det,flush=True)
assert det!=0
remainders={}
for d in (3,4,6):
 phi=S.Poly(S.cyclotomic_poly(d,L),L)
 rem=S.rem(S.Poly(det,L),phi).as_expr()
 assert rem!=0
 remainders[d]=str(rem)
 print('d=',d,'remainder=',rem,flush=True)
result={'nodes':list(zip(a,b)),'D':str(D.as_expr()),'A_basis':list(map(str,A)),'B_basis':list(map(str,B)),
        'rows':list(range(9)),'columns':[(j+1,k+1) for j in range(3) for k in range(3)],
        'minor':[[str(x) for x in minor.row(j)] for j in range(9)],
        'determinant':str(det),'cyclotomic_remainders':remainders,
        'exact_rank':9,'interpretation':'multiplication on nodal genus-four curve; smoothing of exact-order torsion yields rank 9 on smooth covers'}
Path(__file__).with_name('nodal_rank_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
