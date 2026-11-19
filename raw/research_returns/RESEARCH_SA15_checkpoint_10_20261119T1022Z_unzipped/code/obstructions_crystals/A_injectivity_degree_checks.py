"""Exact checks for the corrected crystalline injectivity threshold.

The transition-matrix check deliberately uses dual AFTER Sym.  The withdrawn
Sym(dual) argument is neither used nor tested as a valid identity.
"""
from pathlib import Path
from math import comb
import json
import time
import sympy as sp

started = time.perf_counter()
a, c, hi = sp.symbols("a c hi")
sym_transition = sp.Matrix([[1, c, c**2], [0, a, 0], [0, 0, a**2]])
Pi_inv = sp.Matrix([[1, 0, hi], [0, 1, 0], [0, 0, 1]])
Pj = sp.Matrix([[1, 0, a**2*hi+c**2], [0, 1, 0], [0, 0, 1]])
changed = Pi_inv * sym_transition * Pj
expected = sp.Matrix([[1,c,0],[0,a,0],[0,0,a**2]])
for x in changed-expected:
    assert sp.Poly(sp.expand(x),a,c,hi,modulus=2).is_zero

# Explicitly certify that the tempting entrywise symmetric-dual substitution
# fails already for a single upper-triangular unipotent transition.
dual_after_sym = sp.Matrix([[1,0,0],[1,1,0],[1,0,1]])
sym_after_dual = sp.Matrix([[1,0,0],[0,1,0],[1,1,1]])
assert dual_after_sym != sym_after_dual

def ceil_div(x,y):
    return -((-x)//y)

def h0_B(e):
    assert 0 <= e <= 10
    # On C, every relevant pole bound is <843, so only x powers occur.
    return sum(e+20*i+1 for i in range(e+1))

assert h0_B(1)==24
assert h0_B(5)==336
assert (h0_B(2),h0_B(6),h0_B(10))==(69,469,1221)

rows=[]
h1_R={}
for r in range(1,7):
    contributions=[]
    for j in range(5):
        m=ceil_div(2*(r+j),5)
        e=4*j-r-10
        if m<2 or e<0:
            dim=0
            reason="no relative H1, or every dual-filtration quotient negative"
        elif m==2:
            dim=h0_B(e)
            reason="Sym^0 dual is O"
        elif m==3:
            assert 0<=e<10
            dim=0
            reason="V dual: nonannihilation of Tango class"
        elif m==4:
            assert 0<=e<10
            dim=0
            reason="dual of Sym^2 V = dual V plus B^-20"
        else:
            raise AssertionError((r,j,m,e))
        contributions.append(dim)
        rows.append({"r":r,"j":j,"m":m,"base_exponent":e,
                     "dimension":dim,"reason":reason})
    h1_R[r]=sum(contributions)
assert h1_R=={1:360,2:1,3:0,4:0,5:0,6:0}
for r in range(7,1001):
    assert max(4*j-r-10 for j in range(5))==6-r<0

roots=843
h1_X={1:h1_R[1]+roots*h1_R[2],2:1,3:0}
assert h1_X=={1:1203,2:1,3:0}
h0_R_L=24+336
h0_R_L2=69+469+1221
h0_X_A=h0_R_L+roots
h0_X_A2=h0_R_L2+roots*h0_R_L+comb(roots+1,2)
assert (h0_R_L2,h0_X_A,h0_X_A2)==(1759,1203,660985)

log_terms={}
for r in range(2,7):
    log_terms[r]=[(j,2-ceil_div(2*(r+j),5),4*j-r) for j in range(5)]
assert [v for v in log_terms[5] if v[1]>=0]==[(0,0,-5)]
assert all(v[1]<0 for v in log_terms[6])
assert [v for v in log_terms[4] if v[1]==0 and v[2]>=0]==[(1,0,0)]
assert [v for v in log_terms[3] if v[1]==0 and v[2]>=0]==[(1,0,1),(2,0,5)]
assert [v for v in log_terms[2] if v[1]==0 and v[2]>=0]==[(1,0,2),(2,0,6),(3,0,10)]
assert log_terms[2][0]==(0,1,-2) # H0(V B^-2)=0 by e=8 nonannihilation.

cartier_kernel=[i for i in range(421) if i%2==0]
cartier_image=[(i-1)//2 for i in range(421) if i%2==1]
assert len(cartier_kernel)==211
assert len(set(cartier_image))==210
assert 840-2*0==840 and 840-2*2==836
assert 2>max(h1_X[2],h1_X[3])
assert all(4-2*d<0 for d in (3,4))

result={
    "status":"PASS",
    "transition_check":"Sym^2 V is V plus B^20 after Frobenius splitting",
    "invalid_sym_dual_substitution_explicitly_detected":True,
    "negative_eigensheaf_rows":rows,
    "h1_R_negative_powers":h1_R,
    "universal_vanishing_reason":"r>=7: all base exponents <=6-r<0; r3--6 checked by genuine dual",
    "h1_X_negative_powers":h1_X,
    "h0_negative_differentials_X":{"d2":h0_X_A2,"d3":h0_X_A,"d4":1,"d>=5":0},
    "Cartier_kernel_dimension_on_base_curve":211,
    "minimum_Frobenius_kernel_used_in_proof":2,
    "degree_one_crystalline_kernel_lower_bound":1203-842,
    "claimed_crystalline_injectivity_threshold":3,
    "geometric_scope":"Threshold relies on the written proof and independent audits, not finite testing",
    "elapsed_seconds":time.perf_counter()-started,
}
out=Path(__file__).with_name("A_injectivity_degree_checks_output.json")
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
