#!/usr/bin/env python3
"""Exact eight-generator exterior checks for SF-E823.

The Atiyah/Ext partial-trace theorem is proved in the accompanying text,
not by this finite exterior calculation.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json
import sympy as s

def clean(a):
    return {m:s.expand(c) for m,c in a.items() if s.expand(c)!=0}

def add(*args):
    out={}
    for a in args:
        for m,c in a.items():out[m]=out.get(m,0)+c
    return clean(out)

def scale(a,c):return clean({m:c*v for m,v in a.items()})

def wedge(a,b):
    out={}
    for i,c in a.items():
        for j,d in b.items():
            if i&j:continue
            inv=sum((j&((1<<k)-1)).bit_count() for k in range(8) if (i>>k)&1)
            out[i|j]=out.get(i|j,0)+(-1)**inv*c*d
    return clean(out)

def power(a,n):
    out={0:1}
    for _ in range(n):out=wedge(out,a)
    return out

def exp(a):return add(*(scale(power(a,n),Q(1,factorial(n))) for n in range(5)))

def con(a,k):
    return clean({m^(1<<k):(-1)**(m&((1<<k)-1)).bit_count()*c
                  for m,c in a.items() if (m>>k)&1})

def pi(a,i,j):return con(con(a,i),j)

one={0:1}
omega=[{(1<<i)|(1<<(i+4)):1} for i in range(4)]
plus=add(omega[0],omega[1]);minus=add(omega[2],omega[3]);theta=add(plus,minus)
k,q=s.symbols('k q',nonzero=True)
v=wedge(add(one,scale(power(plus,2),-q/2)),add(one,scale(power(minus,2),-q/2)))
D=scale(theta,k)
F=add(one,scale(power(D,3),-2),scale(power(D,4),4))
H=add(v,scale(power(D,3),2),scale(power(D,4),-4))
assert wedge(H,F)==v
checks=[]
for i,j,other in [(0,1,minus),(2,3,plus)]:
    plane=plus if i==0 else minus
    eta=scale(pi(power(plane,2),i,j),Q(1,2))
    assert add(pi(v,i,j),scale(wedge(eta,v),q))=={}
    obstruction=pi(scale(power(D,3),-2),i,j)
    expected=scale(wedge(eta,other),-12*k**3)
    assert obstruction==expected and obstruction
    checks.append({'plane':'plus' if i==0 else 'minus',
                   'eta':{str(m):str(c) for m,c in eta.items()},
                   'cubic_obstruction':{str(m):str(c) for m,c in obstruction.items()}})

# An exact non-diagonal B checks all Clifford sign conventions on the full
# exterior basis. This is a specified finite check, not a general-B proof.
Bmat=[[2,1,-1,3],[1,-2,2,1],[-1,2,1,-2],[3,1,-2,4]]
B=add(*({(1<<i)|(1<<(j+4)):Bmat[i][j]} for i in range(4) for j in range(4)))
eB=exp(B);emB=exp(scale(B,-1));assert wedge(eB,emB)==one
def shifted_con(a,i):return add(con(a,i),wedge(con(B,i),a))
for i,j in [(0,1),(2,3)]:
    for m in range(256):
        a={m:1}
        direct=wedge(emB,pi(wedge(eB,a),i,j))
        shifted=shifted_con(shifted_con(a,i),j)
        assert direct==shifted
    plane=plus if i==0 else minus
    eta=scale(pi(power(plane,2),i,j),Q(1,2))
    sheared_character=wedge(emB,v)
    xi_B_action=add(shifted_con(shifted_con(sheared_character,i),j),
                    scale(wedge(eta,sheared_character),q))
    assert xi_B_action=={}

out={'result':'PASS','symbolic_parameters':['k','q'],
     'entire_compensated_character':True,'both_balanced_cap_kernels':True,
     'both_nonzero_cubic_obstructions':checks,
     'B_shear_basis_checks':512,'B_matrix':Bmat,
     'limits':'No computation of actual Ext, partial trace, a finite action, or semiregularity. The general-B identity is proved algebraically in the text; its displayed matrix is a finite exact sign check.'}
Path(__file__).with_name('rm_tensor_surface_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
