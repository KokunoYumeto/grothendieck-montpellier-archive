#!/usr/bin/env python3
"""Exact finite algebra for SF-E809--E810.

Checks exterior ranks, common annihilators and Chern/Euler formulas. It does
not prove any sheaf/Ext identification, trace naturality or equivariance; the
complete proofs of those statements are in ci_secant_obstruction_draft.md.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as S

DIM = 8

def basis(k):
    return [sum(1 << i for i in c) for c in combinations(range(DIM), k)]

def wedge(x, y):
    out = {}
    for a, av in x.items():
        for b, bv in y.items():
            if a & b:
                continue
            parity = sum((b & ((1 << i) - 1)).bit_count()
                         for i in range(DIM) if a >> i & 1)
            m = a | b
            out[m] = out.get(m, 0) + (-1)**parity * av * bv
    return {m:S.expand(c) for m,c in out.items() if S.expand(c) != 0}

def add(*terms):
    out = {}
    for scale, term in terms:
        for m,c in term.items():
            out[m] = out.get(m,0) + scale*c
    return {m:S.expand(c) for m,c in out.items() if S.expand(c) != 0}

def graph(t):
    # e_1,...,e_4,p_1,...,p_4; v_t = product (p_i - t e_i).
    out = {0:1}
    for i in range(4):
        out = wedge(out, {1 << (i+4):1, 1 << i:-t})
    return out

def wedge_matrix(v, k):
    target = basis(k+4)
    cols = [wedge({m:1},v) for m in basis(k)]
    return S.Matrix([[col.get(m,0) for col in cols] for m in target])

two, six = basis(2), basis(6)
K = [{(1 << i)|(1 << (i+4)):1} for i in range(4)]
for i,j in combinations(range(4),2):
    K.append({(1 << i)|(1 << (j+4)):1,
              (1 << j)|(1 << (i+4)):1})
Kmat = S.Matrix([[k.get(m,0) for k in K] for m in two])
assert Kmat.rank() == 10

complete_intersections = []
for a,b in [(1,2),(2,4),(3,7),(5,11)]:
    v = add((1,graph(-a)),(1,graph(-b)),(-1,graph(-(a+b))))
    M = wedge_matrix(v,2)
    assert M.rank() == 18
    assert M*Kmat == S.zeros(28,10)
    # Point traces e_1 e_2 e_3 e_4 p_i p_j belong to the CI image.
    point_cols=[]
    for i,j in combinations(range(4,8),2):
        mask=15|(1 << i)|(1 << j)
        point_cols.append(S.Matrix([int(m==mask) for m in six]))
    P=S.Matrix.hstack(*point_cols)
    assert P.rank()==6
    assert M.row_join(P).rank()==18
    complete_intersections.append({"a":a,"b":b,"cap_rank":18,
                                    "point_image_rank":6,
                                    "CI_plus_point_image_rank":18})

# The full common annihilator of L tensor M in degree five.
mixed=[(1 << i)|(1 << j) for i in range(4) for j in range(4,8)]
five,seven=basis(5),basis(7)
blocks=[]
for k in mixed:
    cols=[wedge({k:1},{m:1}) for m in five]
    blocks.append(S.Matrix([[col.get(m,0) for col in cols] for m in seven]))
ann=S.Matrix.vstack(*blocks)
ns=ann.nullspace()
assert len(ns)==8
extreme=[i for i,m in enumerate(five) if (m&15).bit_count() in (1,4)]
assert len(extreme)==8
assert all(all(v[i]==0 for i in range(len(five)) if i not in extreme)
           for v in ns)
secant={15:2,240:3}
assert wedge_matrix(secant,1).rank()==8
assert wedge_matrix(secant,2).rank()==12

# Symbolic, not sampled, moment determinant and Chern/Euler identities.
a,b,z=S.symbols('a b z', positive=True)
col=lambda t:S.Matrix([1,t,t*t])
H=sum((w*col(t)*col(t).T for t,w in [(-a,1),(-b,1),(-a-b,-1)]),S.zeros(3))
detH=S.factor(H.det())
assert S.simplify(detH+a*a*b*b*(a-b)**2)==0
p=a*b
A=2*p
B=3*p*(a+b)
Cactual=-4*p*(a*a+b*b)-6*p*p
Creq=A*A-B*B/A
N=p*(a-b)**2/2
D=p+S.Rational(9,4)*(a-b)**2
assert S.simplify(Cactual-Creq-N)==0
chi=2*Creq+6*A*A
assert S.simplify(chi+4*p*D)==0
assert S.simplify(chi+p*(4*p+9*(a-b)**2))==0
e1=a**4+b**4-(b-a)**4+10+4*N
e2=18+6*N
assert S.simplify(2-2*e1+e2-chi)==0

# Reconstruct the entire truncated two-exponential moment sequence from
# the root recurrence, without choosing an algebraic square-root branch.
root_sum=-B/A
root_product=A
moments=[S.Integer(1),S.Integer(0)]
for k in range(2,5):
    moments.append(S.factor(root_sum*moments[-1]-root_product*moments[-2]))
assert S.simplify(moments[2]+A)==0
assert S.simplify(moments[3]-B)==0
assert S.simplify(moments[4]-Creq)==0
character=sum(moments[k]*z**k/S.factorial(k) for k in range(5))
koszul=S.series(S.exp(-a*z)+S.exp(-b*z)-S.exp(-(a+b)*z),z,0,5).removeO()
assert S.simplify(character-koszul+N*z**4/24)==0

examples=[]
for av,bv in [(1,2),(2,4)]:
    sub={a:av,b:bv}
    vals={"a":av,"b":bv,"N":int(N.subs(sub)),
          "D":str(D.subs(sub)),"chi":int(chi.subs(sub)),
          "Ext1":int(e1.subs(sub)),"Ext2":int(e2.subs(sub)),
          "trace_rank":18,"trace_kernel":int((6*N).subs(sub))}
    assert vals['N']>0
    assert vals['chi']==2-2*vals['Ext1']+vals['Ext2']
    examples.append(vals)

out={
 "status":"PASS",
 "arithmetic":"exact integers/rationals and symbolic SymPy identities",
 "CI_checks":complete_intersections,
 "generic_three_slope_moment_determinant":str(detH),
 "secant_cap1_rank":8,
 "secant_cap2_rank":12,
 "common_mixed_annihilator_degree5_dimension":8,
 "common_annihilator_bidegrees":[[4,1],[1,4]],
 "character_identity":"entire degree<=4 exponential character verified symbolically",
 "chi_formula":str(S.factor(chi)),
 "examples":examples,
 "limits":"No sheaf existence, self-Ext, equivariance or semiregularity is certified by finite linear algebra alone; see full proof."
}
Path(__file__).with_name('ci_secant_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
