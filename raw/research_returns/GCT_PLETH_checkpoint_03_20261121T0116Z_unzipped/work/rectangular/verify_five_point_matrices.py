"""Independent exact audit of the displayed T038 matrices and cubic map."""
from pathlib import Path
import sympy as s

out = []
x, y, z, w = v = s.symbols("x y z w")
A, B, C, D, E = u = s.symbols("A B C D E")
f = s.Matrix([x*z-x*y, x*w-x*y, y*z-x*y, y*w-x*y, z*w-x*y])
M = s.Matrix([
    [y-w, y, y, y-w, 0],
    [z-y, -y, -y, -y, -y],
    [0, -x, -w, -x, -w],
    [0, x, z, 0, 0],
    [0, 0, 0, x, y]])
N = s.Matrix([y*(x-w), z*(y-w), x*(w-y), y*(w-z), x*(z-w)])
P = s.Matrix([[0,0,0,-1,0], [0,0,1,0,-1], [0,1,0,0,0],
              [0,0,-1,1,0], [1,-1,0,0,0]])
assert all(s.expand(q) == 0 for q in f.T*M)
assert all(s.expand(q) == 0 for q in M*N)
assert s.factor(M[:4,:4].det()) == x*(z-w)*(x*y-w*z)
assert s.gcd_list(list(N)) == 1
assert all(s.expand(q) == 0 for q in N-P*f) and P.det() == -1
K = M*P
assert K + K.T == s.zeros(5)
pf = []
for i in range(5):
    J = [j for j in range(5) if j != i]
    a,b,c,d = J
    pf.append(s.expand((-1)**i*(K[a,b]*K[c,d]-K[a,c]*K[b,d]+K[a,d]*K[b,c])))
assert s.Matrix(pf) == f
out.append("PASS matrix products, primitive kernel, nonzero minor, P and signed Pfaffians")

F = A*D*(E-B-C)-B*C*(E-A-D)
t = s.Matrix([A+B-C+D-E, -A+B+C-D-E, -A+B+C-D+E,
              -A-B-C+D+E, A-B-C-D+E, A-B+C+D-E])
assert s.expand(F.subs(dict(zip(u,f)), simultaneous=True)) == 0
assert sum(t) == 0
assert s.expand(sum(q**3 for q in t)+24*F) == 0
assert t.jacobian(u).rank() == 5
assert s.Poly(F,E).LC() == A*D-B*C
assert s.expand(s.Poly(F,E).TC().subs({A:1,B:2,C:3,D:6})) == 12
out.append("PASS quadratic substitution, primitive cubic, six-form rank and exact -24 scalar")

# Compute every group element on E from its action on the five literal
# affine representatives ell1,...,ell4,ell5=-(ell1+...+ell4).
# No use of the producer's character/action code.
import itertools
ell = [s.eye(4)[:,i] for i in range(4)] + [-s.ones(4,1)]
monomials = [x*y,x*z,x*w,y*z,y*w,z*w]
fc = s.Matrix([[s.Poly(fi,v).coeff_monomial(q) for q in monomials] for fi in f])
six_class = {}
generator_actions = []
def ctype(p):
    seen = set()
    ans = []
    for j in range(len(p)):
        if j in seen:
            continue
        k,n = j,0
        while k not in seen:
            seen.add(k)
            n += 1
            k = p[k]
        ans.append(n)
    return tuple(sorted(ans, reverse=True))

for perm in itertools.permutations(range(5)):
    g = s.Matrix.hstack(*(ell[perm[i]] for i in range(4)))
    sign = int(g.det())
    gv = g.inv()*s.Matrix(v)
    gf = [s.expand(q.subs(dict(zip(v,gv)), simultaneous=True)) for q in f]
    transforms = []
    for q in gf:
        coeff = s.Matrix([s.Poly(q,v).coeff_monomial(m) for m in monomials])
        c = fc.T.gauss_jordan_solve(coeff)[0]
        assert s.expand(q-sum(c[j]*f[j] for j in range(5))) == 0
        transforms.append(sum(c[j]*u[j] for j in range(5)))
    gt = [s.expand(q.subs(dict(zip(u,transforms)), simultaneous=True)) for q in t]
    action = []
    for q in gt:
        hits = [j for j in range(6) if s.expand(q-sign*t[j]) == 0]
        assert len(hits) == 1
        action.append(hits[0])
    assert len(set(action)) == 6
    ct, six = ctype(perm), ctype(action)
    if ct in six_class:
        assert six_class[ct] == six
    six_class[ct] = six
    for i in range(4):
        trans = list(range(5))
        trans[i],trans[i+1] = trans[i+1],trans[i]
        if tuple(trans) == perm:
            generator_actions.append((i+1, tuple(j+1 for j in action)))

expected = {(1,1,1,1,1):(1,1,1,1,1,1), (2,1,1,1):(2,2,2),
            (2,2,1):(2,2,1,1), (3,1,1):(3,3), (3,2):(6,),
            (4,1):(4,1,1), (5,):(5,1)}
assert six_class == expected
out.append("PASS all 120 literal signed permutation actions on the six displayed forms")
for ct in sorted(six_class):
    out.append(f"class {ct} -> {six_class[ct]}")
for i,p in sorted(generator_actions):
    out.append(f"adjacent transposition ({i},{i+1}): sign -1, six permutation {p}")
path = Path(__file__).with_name("FIVE_POINT_MATRIX_INDEPENDENT_CHECK.txt")
path.write_text("\n".join(out)+"\n")
print("\n".join(out))
