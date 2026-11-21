"""Independent T_p on M_k(Gamma_0(3), chi_-3), k odd, basis a^{k-3j} b^j (a = weight-1 hexagonal theta, b = 27 eta(3t)^9/eta(t)^3).
Cuspidal char poly = charpoly / (x - (1 + p^{k-1}))^2 (p = 1 mod 3). Compares with KTOWER evidence/gl2_uniform.json.
usage: gl2_check.py k p json"""
import sys, json
from sympy import Matrix, symbols, Poly, div
k, p, J = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
dim = k//3 + 1
N = p*(dim + 3) + 5
def chi(d): return 0 if d % 3 == 0 else (1 if d % 3 == 1 else -1)
a = [1] + [6*sum(chi(d) for d in range(1, n+1) if n % d == 0) for n in range(1, N)]
def mul(x, y):
    z = [0]*N
    for i, xi in enumerate(x):
        if xi:
            for j in range(N-i): z[i+j] += xi*y[j]
    return z
# eta(3t)^9/eta(t)^3 = prod (1-q^{3n})^9 (1-q^n)^{-3}
s = [1] + [0]*(N-1)
for n in range(1, N):
    if 3*n < N:
        f = [0]*N; f[0] = 1; f[3*n] = -1
        for _ in range(9): s = mul(s, f)
    g = [0]*N
    for t in range(0, N, n): g[t] = 1
    for _ in range(3): s = mul(s, g)
b = [0] + [27*c for c in s[:N-1]]
basis = []
apow = {0: [1] + [0]*(N-1)}
for e_ in range(1, k+1): apow[e_] = mul(apow[e_-1], a)
bp = [1] + [0]*(N-1)
for j in range(dim):
    basis.append(mul(apow[k-3*j], bp)); bp = mul(bp, b)
M = dim + 3
Bd = Matrix([[f[n] for n in range(dim)] for f in basis])
cols = []
for f in basis:
    t = [f[p*n] + (chi(p)*p**(k-1)*f[n//p] if n % p == 0 else 0) for n in range(M)]
    c = Bd.T.solve(Matrix(t[:dim]))
    assert list(Matrix([[f2[n] for n in range(M)] for f2 in basis]).T*c) == t
    cols.append(list(c))
A = Matrix(cols).T
x = symbols('x')
cp = Poly(A.charpoly(x).as_expr(), x)
E = 1 + p**(k-1)
q, r = div(cp, Poly((x-E)**2, x))
assert r.is_zero
coeffs = [int(c) for c in q.all_coeffs()]
val = int(q.eval(E))
d = json.load(open(J))
e = (k-1)//2
for D in d['degrees']:
    if int(D['e']) == e:
        for R in D['results']:
            if int(R['p']) == p:
                print(f"k={k} p={p}: cusp dim {len(coeffs)-1}; charpoly coefficients match: {coeffs == [int(c) for c in R['charpoly_coefficients']]}; comparison value match: {val == int(R['comparison_value'])}")
