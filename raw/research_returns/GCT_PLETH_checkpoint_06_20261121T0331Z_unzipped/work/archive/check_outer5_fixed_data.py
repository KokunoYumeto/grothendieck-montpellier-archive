"""Independent finite identities supporting complete T038/T039/G017 reviews."""
from itertools import permutations
from pathlib import Path
from math import gcd, comb
import json
import sympy as s

root = Path(__file__).resolve().parent
t = s.symbols("t")
classes = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
sizes = [1,10,15,20,20,30,24]
labels = [(5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1)]
chars = [
    [1,1,1,1,1,1,1], [4,2,0,1,-1,0,-1],
    [5,1,1,-1,1,-1,0], [6,0,-2,0,0,0,1],
    [5,-1,1,-1,-1,1,0], [4,-2,0,1,1,0,-1],
    [1,-1,1,1,-1,-1,1],
]
D = [[0],[1,2,3,4],[2,3,4,5,6],[3,4,5,5,6,7],
     [4,5,6,7,8],[6,7,8,9],[10]]
expected_K = [
    [0,0,1,0,0,0,0], [0,1,1,1,1,0,0],
    [1,1,1,1,1,1,0], [0,1,1,2,1,1,0],
    [0,1,1,1,1,1,1], [0,0,1,1,1,1,0],
    [0,0,0,0,1,0,0],
]

def inner(a,b):
    return s.Rational(sum(c*x*y for c,x,y in zip(sizes,a,b)),120)

assert [[inner(a,b) for b in chars] for a in chars] == s.eye(7).tolist()
K = [[inner([u*r for u,r in zip(chars[2],chars[i])],chars[j])
      for j in range(7)] for i in range(7)]
assert K == expected_K

def tableaux_rows(shape):
    # Fill increasing numbers by recursively adjoining one outer corner.
    out = []
    def rec(current, rows):
        if len(rows) == 5:
            out.append(rows)
            return
        for i in range(len(shape)):
            if current[i] < shape[i] and (i == 0 or current[i] < current[i-1]):
                nxt = list(current); nxt[i] += 1
                rec(nxt,rows+[i])
    rec([0]*len(shape),[])
    return out

for shape,expected in zip(labels,D):
    actual = sorted(sum(5-i for i in range(1,5) if rows[i]>rows[i-1])
                    for rows in tableaux_rows(shape))
    assert actual == expected,(shape,actual)

den = s.prod(1-t**j for j in (2,3,4,5))
symE = [(1-t)/s.prod(1-t**l for l in cyc) for cyc in classes]
for i in range(7):
    rational = sum(s.Rational(sizes[j]*chars[i][j],120)*symE[j] for j in range(7))
    assert s.cancel(rational - sum(t**r for r in D[i])/den) == 0
tagcounts = [sum(K[r][i]*len(D[r]) for r in range(7))+len(D[i])
             for i in range(7)]
assert tagcounts == [6,24,30,36,30,24,6]

x,y,z,w = s.symbols("x y z w")
q = (x,y,z,w)
f = s.Matrix([x*z-x*y,x*w-x*y,y*z-x*y,y*w-x*y,z*w-x*y])
M = s.Matrix([[y-w,y,y,y-w,0],[z-y,-y,-y,-y,-y],
              [0,-x,-w,-x,-w],[0,x,z,0,0],[0,0,0,x,y]])
N = s.Matrix([y*(x-w),z*(y-w),x*(w-y),y*(w-z),x*(z-w)])
P0 = s.Matrix([[0,0,0,-1,0],[0,0,1,0,-1],[0,1,0,0,0],
               [0,0,-1,1,0],[1,-1,0,0,0]])
assert all(s.expand(v)==0 for v in f.T*M)
assert all(s.expand(v)==0 for v in M*N)
assert s.factor(M[:4,:4].det()) == x*(-w+z)*(-w*z+x*y)
assert P0.det() == -1 and all(s.expand(v)==0 for v in N-P0*f)
alt = M*P0
assert alt == -alt.T
pf = []
for i in range(5):
    jj = [j for j in range(5) if j != i]
    a,b,c,d = jj
    pf.append(s.expand((-1)**i*(alt[a,b]*alt[c,d]-alt[a,c]*alt[b,d]+alt[a,d]*alt[b,c])))
assert pf == list(f)
for j,cyc in enumerate(classes):
    traceA = 1+chars[1][j]*t+cyc.count(1)*t**2/(1-t)
    expected = 1-chars[2][j]*t**2+chars[4][j]*t**3-chars[6][j]*t**5
    assert s.cancel(traceA/symE[j]-expected)==0

A,B,C,Dd,Ev = s.symbols("A B C D E")
u = (A,B,C,Dd,Ev)
F = A*Dd*(Ev-B-C)-B*C*(Ev-A-Dd)
subf = dict(zip(u,list(f)))
assert s.expand(F.subs(subf, simultaneous=True)) == 0
six = [A+B-C+Dd-Ev,-A+B+C-Dd-Ev,-A+B+C-Dd+Ev,
       -A-B-C+Dd+Ev,A-B-C-Dd+Ev,A-B+C+Dd-Ev]
assert sum(six) == 0
assert s.expand(sum(a**3 for a in six)+24*F) == 0
assert s.Matrix([[a.coeff(v) for v in u] for a in six]).rank() == 5
sixq = [s.expand(a.subs(subf, simultaneous=True)) for a in six]
identity = tuple(range(5))
def compose(g,h): return tuple(g[h[i]] for i in range(5))
def inverse(g): return tuple(g.index(i) for i in range(5))
def subgroup(g):
    a,seq=identity,[]
    while a not in seq:
        seq.append(a);a=compose(a,g)
    return tuple(sorted(seq))
HH = sorted(set(subgroup(g) for g in permutations(range(5)) if len(subgroup(g))==5))
assert len(HH)==6
def conj(g,H):
    return tuple(sorted(compose(compose(g,h),inverse(g)) for h in H))
generator_perms = []
for i in range(4):
    g=list(identity);g[i],g[i+1]=g[i+1],g[i];g=tuple(g)
    subs = dict(zip(q,q))
    if i<3:
        subs[q[i]],subs[q[i+1]]=q[i+1],q[i]
    else:
        subs=dict(zip(q,(x-w,y-w,z-w,-w)))
    image = [HH.index(conj(g,H)) for H in HH]
    for j in range(6):
        assert s.expand(sixq[j].subs(subs,simultaneous=True)+sixq[image[j]])==0
    generator_perms.append(image)

KK = s.Matrix([
    [0,Ev-B,0,-C,-B*C+B*Dd+C*Dd-Dd*Ev],
    [0,A-Ev,Dd,0,-A*C+A*Dd-C*Dd+C*Ev],
    [Dd-Ev,0,0,A,-A*B+A*Dd-B*Dd+B*Ev],
    [Ev-C,0,-B,0,A*B+A*C-A*Ev-B*C],
    [C-Dd,B-A,0,0,-A*Dd+B*C]])
assert s.expand(KK.det()-3*F**2)==0
adj = KK.adjugate()
PP = adj.applyfunc(lambda a:s.cancel(a/F))
assert all(s.denom(a)==1 for a in PP)
assert list(PP[4,:]) == [-a for a in u]
assert all(s.expand(a)==0 for a in PP*KK-3*F*s.eye(5))
assert all(s.expand(a)==0 for a in KK*PP-3*F*s.eye(5))
assert s.expand(PP.det()-81*F**3)==0
h = [f[0]*(x+y+z-2*w), f[1]*(x+y+w-2*z),
     f[2]*(x+y+z-2*w), f[3]*(x+y+w-2*z),
     z*w*(z+w-2*x-2*y)-x*y*(x+y-2*z-2*w)]
for i in range(4):
    for j in range(5):
        assert s.expand(f[j]*q[i]**2-PP[i,j].subs(subf,simultaneous=True)-q[i]*h[j])==0
assert s.factor(PP[:2,:2].det()) == -3*A*B*(A*Dd-B*C)

expected_h = [
 [0,1,1,1,2,2,3,3,3,4,3,3,3,2,2,1,1,1,0,0],
 [1,1,2,5,6,9,11,12,14,14,14,13,12,10,8,6,3,2,1,0],
 [0,1,3,5,8,11,13,16,17,17,18,17,15,13,10,7,5,2,1,1],
 [0,1,3,5,9,12,16,19,20,22,21,21,19,16,13,9,6,3,1,0],
 [0,1,2,4,7,10,13,15,17,18,18,17,16,14,11,8,5,3,1,0],
 [0,0,1,3,5,8,10,12,14,14,15,14,13,12,9,7,4,2,1,0],
 [0,0,0,1,1,1,3,3,3,4,3,4,4,2,3,2,1,1,0,0]]
target_trace = [(4+5*t)/(1-t)**4, (2-t)/((1-t)**3*(1+t)),
                t/(1-t**2)**2,1/(1-t**3),-1/(1-t**3),
                t/(1-t**4),-(1-t)/(1-t**5)]
def U_power_trace(cyc,r):
    cp=[]
    for l in cyc: cp += [l//gcd(l,r)]*gcd(l,r)
    m1,m2=cp.count(1),cp.count(2)
    return comb(m1,2)+m2-m1
traces = []
for j,cyc in enumerate(classes):
    power = [0]+[U_power_trace(cyc,r) for r in range(1,6)]
    el = [s.Integer(1)]
    for k in range(1,6):
        el.append(s.expand(sum((-1)**(r-1)*el[k-r]*power[r] for r in range(1,k+1))/k))
    det = sum((-1)**k*el[k]*t**k for k in range(6))
    trace = s.cancel((chars[1][j]+t-chars[2][j]*t**2)/det)
    assert s.cancel(trace-target_trace[j])==0
    traces.append(trace)
params = s.prod(1-t**r for r in (2,4,6,10))
Htr = [s.cancel(params*tr) for tr in traces]
actual_h = []
for i in range(7):
    poly = s.Poly(s.cancel(sum(s.Rational(sizes[j]*chars[i][j],120)*Htr[j] for j in range(7))),t)
    assert poly.degree()<=19
    actual_h.append([int(poly.nth(j)) for j in range(20)])
assert actual_h==expected_h
assert [sum(row) for row in actual_h] == [36,144,180,216,180,144,36]
assert sum(sum(row)*chars[i][0] for i,row in enumerate(actual_h))==4320
assert [s.Poly(p,t).eval(1) for p in Htr] == [4320,0,0,0,0,0,0]

# Independent residue-tuple count for the fixed-arithmetic evaluator.
coeff=[1]
for weight in (1,2,3,5):
    out=[0]*(len(coeff)+(30-weight))
    for i,a in enumerate(coeff):
        for r in range(30//weight): out[i+weight*r]+=a
    coeff=out
assert len(coeff)==110
dp=[0]*241;dp[0]=1
for weight in (1,2,3,5):
    for n in range(weight,len(dp)): dp[n]+=dp[n-weight]
for n in range(len(dp)):
    count=sum(coeff[j]*comb((n-j)//30+3,3) for j in range(min(n,109)+1) if (n-j)%30==0)
    assert count==dp[n]

receipt = {
 "status":"PASS",
 "T038":{"resolution_products":2,"alternating_pfaffians":5,
         "equivariant_resolution_rational_identities":7,
         "six_form_generators":4,"six_form_generator_permutations":generator_perms},
 "T039":{"tableaux":26,"symmetric_power_rational_identities":7,
         "tensor_table_entries":49,"tag_counts":list(map(int,tagcounts))},
 "G017":{"matrix_factorizations":2,"substitution_relations":20,
         "rational_characters":7,"table_entries":140,
         "tag_totals":[sum(row) for row in actual_h],
         "residue_formula_arguments_checked":len(dp)},
 "scope":"Finite identities independently executed; complete geometric and algebraic proofs reviewed separately. No claim to rerun the authors' variable coefficient sweeps."
}
(root/"OUTER5_FIXED_DATA_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
