#!/usr/bin/env python3
"""Exact finite certificates for supplementary claims C859 and C860.

C859: exhaustive SL2(F3) generation and the explicit j-function transform.
C860: the unsplit simple-spectrum obstruction over F5; the general lifting
theorem is proved in proof_notes.md, not inferred from this example.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json
import sympy as s

def mul(a,b,p):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%p for i in range(2) for j in range(2))
def inv(a,p):
    assert (a[0]*a[3]-a[1]*a[2])%p==1
    return (a[3]%p,(-a[1])%p,(-a[2])%p,a[0]%p)
I=(1,0,0,1)
gamma=(1,0,1,1)
eta=(2,0,0,1)
sl2={a for a in product(range(3),repeat=4) if (a[0]*a[3]-a[1]*a[2])%3==1}
borel={a for a in sl2 if a[2]==0}
G={mul(mul(gamma,a,3),inv(gamma,3),3) for a in borel}
Gstar={mul(mul(eta,a,3),eta,3) for a in G}
A=mul(mul(gamma,(1,1,0,1),3),inv(gamma,3),3)
B=mul(mul(eta,A,3),eta,3)
gens={'A':A,'B':B,'-I':(2,0,0,2)}
words={I:''};todo=deque([I])
while todo:
    a=todo.popleft()
    for label,b in gens.items():
        c=mul(a,b,3)
        if c not in words:
            words[c]=(words[a]+' '+label).strip();todo.append(c)
assert len(sl2)==24 and len(G)==len(Gstar)==6
assert G!=Gstar and set(words)==sl2
width=next(h for h in range(1,4) if (1,h%3,0,1) in G)
assert width==3
M=s.Matrix([[1,2],[1,3]])
diag_gamma_inv=s.Matrix([[3,0],[-1,1]])
assert M.det()==1
assert M*diag_gamma_inv==s.Matrix([[1,2],[0,3]])

# Finite products suffice for each reported Fourier coefficient.
q,zeta=s.symbols('q zeta')
N=5
E4=1+240*sum(sum(d**3 for d in s.divisors(n))*q**n for n in range(1,N+1))
delta=q*s.prod((1-q**n)**24 for n in range(1,N+1))
jseries=s.series(E4**3/delta,q,0,4).removeO().expand()
coeff={n:int(jseries.coeff(q,n)) for n in range(-1,4)}
assert [coeff[n] for n in (-1,0,1,2)]==[1,744,196884,21493760]
Fcoeff={n:str(s.rem(s.Poly(coeff[n]*zeta**((2*n)%3),zeta),s.Poly(zeta*zeta+zeta+1,zeta)).as_expr()) for n in range(-1,4)}
assert Fcoeff[-1]=='zeta'
# T changes q3 to zeta*q3, so the leading coefficient changes from zeta to 1.
assert s.rem(s.Poly(zeta*zeta**2,zeta),s.Poly(zeta*zeta+zeta+1,zeta)).as_expr()==1

# A simple spectrum over an algebraic closure need not split over the base.
roots_mod5=[a for a in range(5) if (a*a+2)%5==0]
assert roots_mod5==[]
disc_mod5=(-8)%5
assert disc_mod5!=0
out={
 'C859':{'SL2_F3_order':len(sl2),'Gamma_image_order':len(G),'conjugate_image_order':len(Gstar),
         'distinct_images':G!=Gstar,'generated_order':len(words),'cusp_width':width,
         'A':A,'B':B,'word_for_T':words[(1,1,0,1)],'word_for_S':words[(0,2,1,0)],
         'all_generated_matrices_and_words':[[list(a),words[a]] for a in sorted(words)],
         'Mobius_transform_identity':'[[1,2],[1,3]] * [[3,0],[-1,1]] = [[1,2],[0,3]]',
         'j_coefficients':coeff,'j_shifted_coefficients_in_q3':Fcoeff,
         'leading_coefficient_before_T':'zeta','leading_coefficient_after_T':'1'},
 'C860':{'base_field_counterexample_matrix':[[0,-2],[1,0]],
         'characteristic_polynomial':'X^2+2','roots_in_F5':roots_mod5,
         'discriminant_mod5':disc_mod5,
         'scope':'Shows splitting extension may be necessary; does not prove the general lifting theorem.'}}
outpath=Path(__file__).resolve().parents[1]/'outputs/check_supplement.json'
outpath.parent.mkdir(parents=True,exist_ok=True)
outpath.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
