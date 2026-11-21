"""Exact exterior-algebra check of integral Weil seeds on E^(2n).

Pure Python; no computer algebra library. Q(omega) is Z[w]/(w^2+w+1).
The ordering is x_1,...,x_n,y_1,...,y_n, with e,f for each elliptic curve.
"""
from itertools import product
from math import comb, factorial
import json

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def mul(a,b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def power(a,k):
    r=(1,0)
    for _ in range(k): r=mul(r,a)
    return r
def wedge_sign(a,b):
    if a&b: return 0
    inv=sum((b&((1<<i)-1)).bit_count() for i in range(a.bit_length()) if a&(1<<i))
    return -1 if inv%2 else 1
def pairing(a,b,rank):
    top=(1<<rank)-1
    return sum(c*b.get(top^mask,0)*wedge_sign(mask,top^mask) for mask,c in a.items())

out={}
for n in (2,4):
    g=2*n
    z={0:(1,0)}
    for j in range(g):
        c=(0,1) if j<n else (-1,-1)
        nxt={}
        for mask,v in z.items():
            nxt[mask|(1<<(2*j))]=v
            nxt[mask|(1<<(2*j+1))]=mul(v,c)
        z=nxt
    u={m:c[0] for m,c in z.items() if c[0]}
    v={m:c[1] for m,c in z.items() if c[1]}
    gram=[[(-1)**n*pairing(a,b,2*g) for b in (u,v)] for a in (u,v)]
    want=[[2*3**(n-1),3**(n-1)],[3**(n-1),2*3**(n-1)]]
    assert gram==want,(n,gram)
    all_e=sum(1<<(2*j) for j in range(g))
    one_f=(all_e^(1<<0))|(1<<1)
    assert z[all_e]==(1,0) and z[one_f]==(0,1)
    contributions=[]
    bounds=[0,0]
    for k in range(n+1):
        coeff=power((0,1),k)
        sign_degree=factorial(n)*2**(3*n-k-1)
        for i in (0,1): bounds[i]+=comb(n,k)*abs(coeff[i])*sign_degree
        contributions.append(dict(k_V=k,multiplicity=comb(n,k),omega_power=coeff,each_sign_degree=sign_degree))
    out[str(n)]={"g":g,"integral_basis_certificate":[z[all_e],z[one_f]],"positive_Gram":gram,
                 "Gram_determinant":3**(2*n-1),"basis_cycle_degree_bounds":bounds,
                 "coefficient_expansion":contributions,"raw_multiplier_exponent":2*n}
assert out['2']['basis_cycle_degree_bounds']==[80,80]
assert out['4']['basis_cycle_degree_bounds']==[147456,175104]

# Divisor checks on one E x E. Each ordered wedge e_x,f_x,e_y,f_y.
U={5:1,9:-1,10:1}
V={9:-1,6:1}
theta={3:1,12:1}
def lincomb(*terms):
    d={}
    for c,a in terms:
        for k,x in a.items(): d[k]=d.get(k,0)+c*x
    return {k:x for k,x in d.items() if x}
Gamma1=lincomb((1,theta),(1,V))
Gammaw=lincomb((1,theta),(1,U),(-1,V))
assert pairing(Gamma1,Gamma1,4)==0
assert pairing(Gammaw,Gammaw,4)==0
assert pairing(theta,Gamma1,4)==2
assert pairing(theta,Gammaw,4)==2
assert pairing(Gamma1,Gammaw,4)==3
out['pair_divisors']={"U_self":pairing(U,U,4),"V_self":pairing(V,V,4),
                      "U_V":pairing(U,V,4),"graph_intersection":pairing(Gamma1,Gammaw,4)}
print(json.dumps(out,indent=2))
