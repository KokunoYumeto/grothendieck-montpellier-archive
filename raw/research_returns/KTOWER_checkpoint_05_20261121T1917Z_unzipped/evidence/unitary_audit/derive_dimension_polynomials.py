"""Derive the quasipolynomial from the proved Burnside formula, not a fit."""
from itertools import product
from pathlib import Path
import json
import sympy as s

n=s.symbols('n',integer=True,nonnegative=True)
coeff=[0]*16
for residual in product(range(6),repeat=3):
    coeff[sum(residual)]+=1

def full(r):
    identity=0
    for j in range(16):
        if (r-j)%6==0:
            u=2*n+(r-j)//6
            identity+=coeff[j]*((u+1)*(u+2)/2)**2
    q=n+(r//2+1)//6
    rem=(r//2+1)%6
    transposition=6*q*q+2*q*rem+rem
    cycle=int(r%3==0)
    return s.expand((identity+3*transposition+2*cycle)/6)

if __name__=='__main__':
    A=[full(r) for r in range(12)]
    rows=[]
    for r in range(12):
        previous=A[r-1] if r else A[11].subs(n,n-1)
        D=s.factor(A[r]-previous)
        rows.append({'residue':r, 'A_polynomial':str(s.factor(A[r])),
                     'D_polynomial':str(D), 'D_expanded':str(s.expand(D))})
    output={'method':'symbolic substitution into the Burnside formula; no interpolation',
            'residue_coefficients':coeff, 'variable':'d=12*n+r', 'rows':rows}
    Path(__file__).with_name('dimension_polynomials.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(rows,indent=2))
