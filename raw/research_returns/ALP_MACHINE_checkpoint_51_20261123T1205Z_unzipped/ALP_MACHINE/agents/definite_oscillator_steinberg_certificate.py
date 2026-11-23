"""Exact GL_2(F_3), b=3 check of DO033; not a Lean proof."""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

q, a, b = 3, 2, 3

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def mul(x, y):
    return (x[0]*y[0] - x[1]*y[1],
            x[0]*y[1] + x[1]*y[0] - x[1]*y[1])

def conj(x):
    return (x[0] - x[1], -x[1])

def root(n):
    return ((1,0), (0,1), (-1,-1))[n % 3]

def norm(x):
    return x[0]**2 - x[0]*x[1] + x[1]**2

def det(g):
    return (g[0]*g[3] - g[1]*g[2]) % 3

def mm(g, h):
    return tuple(sum(g[2*i+k]*h[2*k+j] for k in range(2)) % 3
                 for i in range(2) for j in range(2))

def line(v):
    if v[0] % 3:
        inv = pow(v[0] % 3, -1, 3)
    else:
        inv = pow(v[1] % 3, -1, 3)
    return tuple(inv*x % 3 for x in v)

def act(g, v):
    return line((g[0]*v[0]+g[1]*v[1], g[2]*v[0]+g[3]*v[1]))

G = [g for g in product(range(3), repeat=4) if det(g)]
flags = sorted({line(v) for v in product(range(3), repeat=2) if any(v)})
v = {L: (0,0) for L in flags}
for t in range(3):
    v[line((t,1))] = root(-t)
assert sum(norm(c) for c in v.values()) == 3
assert tuple(map(sum, zip(*v.values()))) == (0,0)

# m(g) = mn(g)/3 in Q(zeta_3).
mn = {}
for g in G:
    z = (0,0)
    for L in flags:
        z = add(z, mul(conj(v[act(g,L)]), v[L]))
    mn[g] = z
assert mn[(1,0,0,1)] == (3,0)
assert sum(norm(z) for z in mn.values()) == 144

# eta is the nontrivial determinant residue character.
eta = lambda g: 1 if det(g) == 1 else -1
Fn = {g+(0,0): tuple(eta(g)*x for x in mn[g]) for g in G}
for g in G:
    for s in range(3):
        u = (1,s,0,1)
        assert mn[mm(g,u)] == mul(root(s), mn[g])
        lhs = tuple(eta(u)*x for x in Fn[mm(g,u)+(0,0)])
        rhs = mul(root(s), Fn[g+(0,0)])
        assert lhs == rhs

# Full Fourier quotient has N=3^6; coefficient = bn/(3N).
N = 3**6
bn = []
for y in product(range(3), repeat=6):
    z = (0,0)
    for X, val in Fn.items():
        z = add(z, mul(val, root(-sum(x*t for x,t in zip(X,y)))))
    bn.append((y,z))
gamma = Fraction(48, 3*N)
assert sum(Fraction(norm(z), (3*N)**2) for _,z in bn) == gamma
assert gamma == Fraction(16,729)

# Fourier inversion at the unit-valued full-rank matrix.
X0 = (1,0,0,1,0,0)
z = (0,0)
for y, val in bn:
    z = add(z, mul(val, root(sum(x*t for x,t in zip(X0,y)))))
assert z == (3*N,0)

def vp(n,p):
    k=0
    while n and n%p == 0:
        n//=p
        k+=1
    return k

actual_costs = {}
for aux_q in (113,281,337):
    val = sum(vp(aux_q**i-1,11) for i in range(1,7))
    actual_costs[str(aux_q)] = val
assert actual_costs == {'113':1,'281':0,'337':0}

out = {
    'status':'PASS', 'model':'GL_2(F_3), b=3, nontrivial determinant splitting',
    'group_order':len(G), 'flags':len(flags), 'steinberg_dimension':3,
    'generic_vector_norm_squared':3,
    'matrix_coefficient_square_sum':'16',
    'raw_schwartz_norm_squared':str(gamma),
    'fourier_quotient_size':N,
    'nonzero_fourier_coefficients':sum(z!=(0,0) for _,z in bn),
    'full_rank_value':'1', 'generic_covariance_all_group_elements':True,
    'rank6_v11_GL_orders':actual_costs,
    'scope':'Exact finite model diagnostic; general proof is DO033.'
}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
