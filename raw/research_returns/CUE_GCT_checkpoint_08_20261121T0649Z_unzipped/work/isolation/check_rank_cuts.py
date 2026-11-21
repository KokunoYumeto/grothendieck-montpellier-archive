"""Exact finite rank-cut and corank-budget checks supplementing I-19/I-20."""
from pathlib import Path
from random import Random
import sympy as sp

rng = Random(1920)
x = sp.Symbol('x')
lines = []
for w, r in [(3, 1), (3, 2), (4, 2), (4, 3)]:
    while True:
        left = sp.Matrix(w, r, lambda i, j: rng.randrange(-2, 3) + rng.randrange(-2, 3)*x)
        right = sp.Matrix(r, w, lambda i, j: rng.randrange(-2, 3) + rng.randrange(-2, 3)*x)
        A = left * right
        M = A[:r, :r]
        determinant = sp.expand(M.det())
        if determinant != 0:
            break
    U = A[:, :r]
    V = M.adjugate() * A[:r, :]
    assert all(sp.expand(entry) == 0 for entry in determinant * A - U * V)
    assert max(sp.degree(entry, x) for entry in U) <= 2
    assert max(sp.degree(sp.expand(entry), x) for entry in V) <= 2*r
    lines.append(f'PASS I-19 pivot-minor factorization over Q[x]: w={w}, rank={r}, entry degree<=2')

y = sp.Symbol('y')
Ax = sp.Matrix([[1, x], [x, x*x]])
Ay = sp.Matrix([[1, y], [y, y*y]])
assert (Ax*Ay)[0,0] == 1+x*y
assert Ax.det() == Ay.det() == 0
lines.append('PASS I-19 shared-cut-variable example: two rank-one matrices produce 1+x*y')

E12 = sp.Matrix([[0,1],[0,0]])
E21 = sp.Matrix([[0,0],[1,0]])
for kappa in range(1,5):
    variables = sp.symbols('z0:'+str(kappa+1))
    row = sp.Matrix([[1,0]])
    for j in range(kappa):
        row = row * (sp.eye(2)+variables[j]*E12) * E21
    row = row * (sp.eye(2)+variables[-1]*E12)
    scalar = sp.expand(row[0,1])
    assert scalar == sp.prod(variables)
    assert sp.Poly(scalar, *variables).terms() == [((1,)*(kappa+1),1)]
    assert E21.rank() == 1
    lines.append(f'PASS I-20 sharp support chain: w=2, total corank={kappa}, minimum support={kappa+1}')

result = '\n'.join(lines)+'\n'
Path(__file__).with_name('rank_cut_computation_checks.txt').write_text(result)
print(result,end='')
